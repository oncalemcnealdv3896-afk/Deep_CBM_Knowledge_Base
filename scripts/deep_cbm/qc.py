"""QC report generator — produce validation reports."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
STATS_DIR = ROOT / "06_Statistics"


def generate_qc_report(
    run_summary: dict[str, Any],
    validation: dict[str, Any],
    run_dir: Path,
) -> Path:
    """Write a QC report markdown and return its path."""
    today = date.today().strftime("%Y%m%d")
    report_path = STATS_DIR / f"QC_Report_{today}_daily_brief_update.md"
    STATS_DIR.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# QC Report — Daily Brief Update {date.today().isoformat()}",
        "",
        "## Summary",
        f"- Status: {run_summary.get('status', '?')}",
        f"- Action: {run_summary.get('action', '?')}",
        f"- Master count: {run_summary.get('master_count_before', '?')} → {run_summary.get('master_count_after', '?')}",
        f"- Added: {run_summary.get('added_count', 0)}",
        f"- Duplicates: {run_summary.get('duplicate_count', 0)}",
        f"- Manual review: {run_summary.get('manual_review_count', 0)}",
        f"- Last ID: {run_summary.get('last_id_before', '?')} → {run_summary.get('last_id_after', '?')}",
        "",
        "## Checks",
        f"- [{'x' if run_summary.get('id_continuous') else ' '}] ID continuous",
        f"- [{'x' if run_summary.get('doi_duplicates', -1) == 0 else ' '}] DOI duplicates = 0",
        f"- [{'x' if run_summary.get('english_title_duplicates', -1) == 0 else ' '}] English title duplicates = 0",
        f"- [{'x' if run_summary.get('chinese_title_duplicates', -1) == 0 else ' '}] Chinese title duplicates = 0",
        f"- [{'x' if run_summary.get('index_matches_workbook') else ' '}] Index matches workbook",
        f"- [{'x' if not run_summary.get('protected_paths_modified') else ' '}] Protected paths unmodified",
        "",
        "## Errors",
    ]

    for e in run_summary.get("errors", []):
        lines.append(f"- {e}")
    if not run_summary.get("errors"):
        lines.append("- (none)")

    lines += ["", "## Warnings"]
    for w in run_summary.get("warnings", []):
        lines.append(f"- {w}")
    if not run_summary.get("warnings"):
        lines.append("- (none)")

    lines += ["", "## Validation Details"]
    for k, v in validation.items():
        if k not in ("changes",):
            lines.append(f"- {k}: {v}")

    with report_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    return report_path
