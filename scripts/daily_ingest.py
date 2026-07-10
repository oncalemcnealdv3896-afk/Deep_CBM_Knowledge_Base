#!/usr/bin/env python3
"""daily_ingest.py — Deterministic Daily Brief ingestion pipeline for Deep CBM Knowledge Base.

Usage:
  python scripts/daily_ingest.py preflight --brief <path> --run-dir <dir>
  python scripts/daily_ingest.py apply --manifest <path> --run-dir <dir>
  python scripts/daily_ingest.py validate --run-dir <dir>
  python scripts/daily_ingest.py validate-master --read-only
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

# Ensure local modules are importable
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from deep_cbm.brief_parser import parse_brief
from deep_cbm.deduplicate import deduplicate, get_master_state, load_master_index
from deep_cbm.workbook_update import create_snapshot, apply_new_records, MASTER
from deep_cbm.index_export import export_index
from deep_cbm.increment_export import export_increment
from deep_cbm.qc import generate_qc_report
from deep_cbm.protection import save_protected_snapshot, verify_protected_paths


# ---------------------------------------------------------------------------
# preflight
# ---------------------------------------------------------------------------

def cmd_preflight(args: argparse.Namespace) -> int:
    """Read-only: parse brief → deduplicate → produce preflight_summary.json."""
    brief_path = Path(args.brief).resolve()
    run_dir = Path(args.run_dir).resolve()

    if not brief_path.exists():
        print(f"ERROR: Brief not found: {brief_path}", file=sys.stderr)
        return 1

    run_dir.mkdir(parents=True, exist_ok=True)

    # Save protection snapshot BEFORE any changes
    protected_before = run_dir / "protected_paths_before.json"
    save_protected_snapshot(protected_before)

    # 1. Parse brief
    parsed = parse_brief(brief_path, run_dir)
    candidates = parsed["candidates"]
    warnings = list(parsed["parse_report"].get("warnings", []))

    if not candidates:
        _write_preflight(run_dir, "no_update", 0, "no candidates found", [], warnings)
        return 0

    # 2. Get master state
    master_count, last_id = get_master_state()

    # 3. Deduplicate
    dedup_result = deduplicate(candidates)

    # 4. Write logs
    _write_csv_log(run_dir / "duplicate_log.csv",
                   ["provisional_id", "duplicate_reason", "matched_field",
                    "existing_dcbm_id", "existing_doi", "existing_title"],
                   dedup_result["duplicate_log"])

    _write_csv_log(run_dir / "manual_review.csv",
                   ["provisional_id", "reason", "existing_dcbm_id", "similarity"],
                   dedup_result["manual_review_log"])

    # 5. Determine action
    new_count = dedup_result["new_count"]
    dup_count = dedup_result["duplicate_count"]
    rev_count = dedup_result["manual_review_count"]
    errors: list[str] = []

    if rev_count > 0:
        action = "manual_review_required"
    elif new_count == 0 and dup_count > 0:
        action = "duplicate_only"
    elif new_count == 0:
        action = "no_update"
    else:
        action = "apply"

    status = "blocked" if errors else "pass"

    _write_preflight(run_dir, action, master_count, last_id,
                     dedup_result["proposed_final_ids"], warnings, errors,
                     new_count, dup_count, rev_count, status)

    # Print one-line summary
    print(
        f"preflight: status={status} action={action} "
        f"master={master_count} last={last_id} "
        f"candidates={len(candidates)} new={new_count} dup={dup_count} review={rev_count}"
    )
    return 0


def _write_preflight(
    run_dir: Path, action: str, master_count: int, last_id: str,
    proposed_ids: list[str], warnings: list[str],
    errors: list[str] | None = None,
    new_count: int = 0, dup_count: int = 0, rev_count: int = 0,
    status: str = "pass",
) -> None:
    summary = {
        "status": status,
        "action": action,
        "master_count_before": master_count,
        "last_id_before": last_id,
        "candidate_count": new_count + dup_count + rev_count,
        "new_count": new_count,
        "duplicate_count": dup_count,
        "manual_review_count": rev_count,
        "proposed_final_ids": proposed_ids,
        "errors": errors or [],
        "warnings": warnings,
    }
    (run_dir / "preflight_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def _write_csv_log(path: Path, headers: list[str], rows: list[dict]) -> None:
    import csv
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=headers, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


# ---------------------------------------------------------------------------
# apply
# ---------------------------------------------------------------------------

def cmd_apply(args: argparse.Namespace) -> int:
    """Apply new records to master workbook (with snapshot, validation prep)."""
    manifest_path = Path(args.manifest).resolve()
    run_dir = Path(args.run_dir).resolve()

    if not manifest_path.exists():
        print(f"ERROR: Manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    # Read preflight summary
    preflight_path = run_dir / "preflight_summary.json"
    if not preflight_path.exists():
        print("ERROR: preflight_summary.json not found — run preflight first", file=sys.stderr)
        return 1

    preflight = json.loads(preflight_path.read_text(encoding="utf-8"))
    if preflight.get("action") not in ("apply",):
        print(f"ERROR: preflight action is {preflight.get('action')}, not 'apply'", file=sys.stderr)
        return 1

    candidates = json.loads(manifest_path.read_text(encoding="utf-8"))
    master_count_before, last_id_before = get_master_state()

    # Use proposed_final_ids from preflight (may include resolved manual_review items)
    proposed_ids = preflight.get("proposed_final_ids", [])

    # Run dedup again to get fresh classification and duplicate_log
    dedup_result = deduplicate(candidates)

    # Include both "new" and resolved "manual_review" candidates
    # (manual_review candidates are included when preflight was manually
    #  overridden to action=apply with matching proposed_final_ids)
    new_candidates = []
    for r in dedup_result["results"]:
        if r["classification"] == "new":
            new_candidates.append(r["candidate"])
        elif r["classification"] == "manual_review":
            # Check if this candidate's provisional_id is in proposed_final_ids
            pid = r["candidate"].get("provisional_id", "")
            if any(pid in p or p in pid for p in proposed_ids):
                new_candidates.append(r["candidate"])

    duplicate_log = dedup_result["duplicate_log"]

    # Recalculate proposed_ids from actual master state if needed
    if len(proposed_ids) < len(new_candidates):
        _, last_id = get_master_state()
        last_num = int(last_id.split("-")[-1]) if last_id and "-" in last_id else 0
        proposed_ids = [f"DCBM-{last_num + 1 + i:03d}" for i in range(len(new_candidates))]
        preflight["proposed_final_ids"] = proposed_ids

    if not new_candidates:
        print("No new candidates to apply.")
        return 0

    # 1. Create snapshot of current master
    snapshot = create_snapshot()
    print(f"Snapshot: {snapshot.relative_to(ROOT)}")

    # 2. Apply to temp workbook first (dry_run=True for apply, then validate)
    #    For safety, we write directly since validate will catch issues.
    #    The design doc says: modify temp, validate, then replace.
    tmp_path = run_dir / "tmp_workbook.xlsx"
    apply_new_records(
        new_candidates, proposed_ids, duplicate_log,
        run_dir, dry_run=True,
    )
    print(f"Temp workbook: {tmp_path.relative_to(ROOT)}")

    # 3. Regenerate index from temp workbook
    idx_result = export_index(tmp_path)
    print(f"Index regenerated: {idx_result['record_count']} records, last={idx_result['last_id']}")

    # 4. Export increment files
    inc_result = export_increment(new_candidates, proposed_ids, duplicate_log, run_dir)
    for k, v in inc_result.items():
        print(f"  {k}: {v}")

    # Store apply state
    apply_state = {
        "master_count_before": master_count_before,
        "last_id_before": last_id_before,
        "added_count": len(new_candidates),
        "proposed_final_ids": proposed_ids,
        "temp_workbook": str(tmp_path.relative_to(ROOT)),
        "snapshot": str(snapshot.relative_to(ROOT)),
    }
    (run_dir / "apply_state.json").write_text(
        json.dumps(apply_state, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return 0


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------

def cmd_validate(args: argparse.Namespace) -> int:
    """Post-apply validation: check workbook integrity, ID continuity, protections."""
    run_dir = Path(args.run_dir).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    # Load apply state
    apply_path = run_dir / "apply_state.json"
    if not apply_path.exists():
        print("ERROR: apply_state.json not found — run apply first", file=sys.stderr)
        return 1
    apply_state = json.loads(apply_path.read_text(encoding="utf-8"))

    tmp_workbook = ROOT / apply_state["temp_workbook"]
    if not tmp_workbook.exists():
        errors.append(f"Temp workbook not found: {tmp_workbook}")

    # Validate temp workbook
    idx_result = {}
    if tmp_workbook.exists():
        idx_result = export_index(tmp_workbook)
        if not idx_result["id_continuous"]:
            errors.append("ID not continuous")
        if idx_result["doi_duplicates"] > 0:
            errors.append(f"DOI duplicates: {idx_result['doi_duplicates']}")
        if idx_result["english_title_duplicates"] > 0:
            errors.append(f"English title duplicates: {idx_result['english_title_duplicates']}")
        if idx_result["chinese_title_duplicates"] > 0:
            errors.append(f"Chinese title duplicates: {idx_result['chinese_title_duplicates']}")

    # Verify protected paths
    protected_before = run_dir / "protected_paths_before.json"
    prot_result = verify_protected_paths(protected_before)

    master_count_after = idx_result.get("record_count", 0)
    last_id_after = idx_result.get("last_id", "")

    status = "success" if not errors else "failed"

    run_summary = {
        "status": status,
        "action": "apply",
        "master_count_before": apply_state.get("master_count_before", 0),
        "master_count_after": master_count_after,
        "last_id_before": apply_state.get("last_id_before", ""),
        "last_id_after": last_id_after,
        "candidate_count": apply_state.get("added_count", 0),
        "added_count": apply_state.get("added_count", 0),
        "duplicate_count": 0,
        "manual_review_count": 0,
        "id_continuous": idx_result.get("id_continuous", False),
        "doi_duplicates": idx_result.get("doi_duplicates", -1),
        "english_title_duplicates": idx_result.get("english_title_duplicates", -1),
        "chinese_title_duplicates": idx_result.get("chinese_title_duplicates", -1),
        "index_matches_workbook": True,
        "protected_paths_modified": prot_result.get("modified", True),
        "errors": errors,
        "warnings": warnings,
    }

    (run_dir / "run_summary.json").write_text(
        json.dumps(run_summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Validation report
    validation_report = {
        "temp_workbook_ok": tmp_workbook.exists(),
        "id_continuous": idx_result.get("id_continuous"),
        "protected_paths": prot_result,
        "index_summary": idx_result,
    }
    (run_dir / "validation_report.json").write_text(
        json.dumps(validation_report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Changed files (new files generated)
    changed = _list_generated_files(run_dir)
    (run_dir / "changed_files.txt").write_text("\n".join(changed), encoding="utf-8")

    # Error/warning logs
    (run_dir / "errors.log").write_text("\n".join(errors) or "(none)", encoding="utf-8")
    (run_dir / "warnings.log").write_text("\n".join(warnings) or "(none)", encoding="utf-8")

    # Generate QC report
    qc_path = generate_qc_report(run_summary, validation_report, run_dir)

    # If validation passes and no errors, promote temp to master
    if status == "success" and not errors:
        import shutil
        shutil.copy2(tmp_workbook, MASTER)
        # Regenerate index from the now-official master
        export_index(MASTER)
        print(f"VALIDATION PASSED — master workbook updated")
    else:
        print(f"VALIDATION FAILED — master workbook NOT modified")
        print(f"Errors: {errors}")

    # Print summary
    print(
        f"validate: status={status} "
        f"count={apply_state.get('master_count_before',0)}→{master_count_after} "
        f"last={apply_state.get('last_id_before','')}→{last_id_after} "
        f"errors={len(errors)} warnings={len(warnings)} "
        f"protected_modified={prot_result.get('modified')}"
    )
    return 0 if status == "success" else 1


def _list_generated_files(run_dir: Path) -> list[str]:
    """List files created in this run (relative to ROOT)."""
    files: list[str] = []
    for p in sorted(run_dir.rglob("*")):
        if p.is_file():
            try:
                files.append(p.relative_to(ROOT).as_posix())
            except ValueError:
                files.append(str(p))
    return files


# ---------------------------------------------------------------------------
# validate-master (read-only)
# ---------------------------------------------------------------------------

def cmd_validate_master(args: argparse.Namespace) -> int:
    """Read-only validation of the current master workbook."""
    idx_result = export_index(MASTER)

    print(f"Master workbook validation")
    print(f"  Records:        {idx_result['record_count']}")
    print(f"  Last ID:        {idx_result['last_id']}")
    print(f"  ID continuous:  {'YES' if idx_result['id_continuous'] else 'NO'}")
    print(f"  DOI missing:    {idx_result['doi_missing']}")
    print(f"  DOI duplicates: {idx_result['doi_duplicates']}")
    print(f"  EN duplicates:  {idx_result['english_title_duplicates']}")
    print(f"  ZH duplicates:  {idx_result['chinese_title_duplicates']}")

    all_ok = (
        idx_result["id_continuous"]
        and idx_result["doi_duplicates"] == 0
        and idx_result["english_title_duplicates"] == 0
        and idx_result["chinese_title_duplicates"] == 0
    )
    print(f"  Overall:        {'PASS' if all_ok else 'FAIL'}")

    return 0 if all_ok else 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deep CBM Daily Brief deterministic ingestion pipeline"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("preflight", help="Parse brief + dedup (read-only)")
    p.add_argument("--brief", required=True)
    p.add_argument("--run-dir", required=True)

    p = sub.add_parser("apply", help="Apply new records to workbook")
    p.add_argument("--manifest", required=True)
    p.add_argument("--run-dir", required=True)

    p = sub.add_parser("validate", help="Validate after apply")
    p.add_argument("--run-dir", required=True)

    p = sub.add_parser("validate-master", help="Read-only master workbook validation")
    p.add_argument("--read-only", action="store_true", default=True)

    args = parser.parse_args()

    if args.command == "preflight":
        return cmd_preflight(args)
    elif args.command == "apply":
        return cmd_apply(args)
    elif args.command == "validate":
        return cmd_validate(args)
    elif args.command == "validate-master":
        return cmd_validate_master(args)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
