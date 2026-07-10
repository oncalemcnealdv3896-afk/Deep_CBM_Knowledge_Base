"""Parse Deep CBM Daily Brief Markdown into structured candidate manifest."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def parse_brief(brief_path: Path, run_dir: Path) -> dict[str, Any]:
    """Parse a Daily Brief and write candidate_manifest.json + brief_parse_report.json.

    Returns {"candidates": [...], "parse_report": {...}}.
    """
    text = brief_path.read_text(encoding="utf-8")

    # Priority 1: daily_ingest_manifest JSON fenced block
    manifest = _extract_manifest_block(text)
    extraction_method = "manifest_block" if manifest else "markdown_table"

    # Priority 2: parse Matrix-ready rows table
    candidates = _parse_matrix_rows(text) if not manifest else manifest.get("candidates", [])

    # Extract RIS blocks  (one per candidate, delimited by ER -)
    ris_entries = _split_ris_entries(text)

    # Extract BibTeX blocks (one per candidate, separated by blank lines)
    bibtex_entries = _split_bibtex_entries(text)

    # Merge RIS/BibTeX into candidates
    warnings: list[str] = []
    for i, cand in enumerate(candidates):
        if i < len(ris_entries):
            cand["ris"] = ris_entries[i]
        else:
            warnings.append(f"{cand.get('provisional_id','?' )} : missing RIS block")
        if i < len(bibtex_entries):
            cand["bibtex"] = bibtex_entries[i]
        else:
            warnings.append(f"{cand.get('provisional_id','?' )} : missing BibTeX block")

    # Write manifest
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = run_dir / "candidate_manifest.json"
    manifest_path.write_text(
        json.dumps(candidates, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    parse_report = {
        "brief_path": str(brief_path),
        "candidate_count": len(candidates),
        "extraction_method": extraction_method,
        "warnings": warnings,
    }
    (run_dir / "brief_parse_report.json").write_text(
        json.dumps(parse_report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    return {"candidates": candidates, "parse_report": parse_report}


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

# Master workbook columns (27 fields)
# Daily Brief may have 26 columns — missing "埋深/对象深度" at index 16
# We detect cell count and insert empty values for missing columns
MASTER_FIELDS_27 = [
    (0, "seq"),
    (1, "provisional_id"),
    (2, "first_author"),
    (3, "authors"),
    (4, "year"),
    (5, "title_en"),
    (6, "title_zh"),
    (7, "journal"),
    (8, "volume"),
    (9, "issue"),
    (10, "pages_or_article"),
    (11, "doi"),
    (12, "official_url"),
    (13, "document_type"),
    (14, "study_area"),
    (15, "research_object"),
    (16, "burial_depth"),
    (17, "research_purpose"),
    (18, "methods"),
    (19, "findings"),
    (20, "innovation"),
    (21, "limitations"),
    (22, "relevance"),
    (23, "suggested_chapter"),
    (24, "tags"),
    (25, "reading_priority"),
    (26, "verification_status"),
]

# Daily Brief 26-column variant: missing index 16 "埋深/对象深度"
MATRIX_FIELDS_26 = [
    (0, "seq"),
    (1, "provisional_id"),
    (2, "first_author"),
    (3, "authors"),
    (4, "year"),
    (5, "title_en"),
    (6, "title_zh"),
    (7, "journal"),
    (8, "volume"),
    (9, "issue"),
    (10, "pages_or_article"),
    (11, "doi"),
    (12, "official_url"),
    (13, "document_type"),
    (14, "study_area"),
    (15, "research_object"),
    # index 16 "埋深/对象深度" missing in brief → burial_depth stays empty
    (16, "research_purpose"),
    (17, "methods"),
    (18, "findings"),
    (19, "innovation"),
    (20, "limitations"),
    (21, "relevance"),
    (22, "suggested_chapter"),
    (23, "tags"),
    (24, "reading_priority"),
    (25, "verification_status"),
]

SKIP_VALUES = {"待定", "TBD", "待全文核验", ""}


def _extract_manifest_block(text: str) -> dict[str, Any] | None:
    """Extract ``daily_ingest_manifest`` JSON fenced block."""
    pattern = r"```(?:json)?\s*\n\s*\{[^}]*\"candidates\"[^}]*\}.*?\n```"
    for match in re.finditer(pattern, text, re.DOTALL | re.IGNORECASE):
        try:
            inner = re.sub(r"^```(?:json)?\s*\n|\n\s*```$", "", match.group(0), flags=re.MULTILINE)
            return json.loads(inner)
        except json.JSONDecodeError:
            continue
    return None


def _parse_matrix_rows(text: str) -> list[dict[str, Any]]:
    """Parse candidates from the Matrix-ready-rows markdown table.

    Handles both 27-column (full master) and 26-column (missing 埋深/对象深度)
    Daily Brief tables.
    """
    candidates: list[dict[str, Any]] = []
    in_table = False

    for line in text.split("\n"):
        stripped = line.strip()

        # Detect table header
        if "| 序号 |" in stripped or "| 序号 | 文献ID |" in stripped:
            in_table = True
            continue
        if in_table and stripped.startswith("|---"):
            continue
        if not in_table:
            continue

        if not stripped.startswith("|"):
            in_table = False
            continue

        cells = [c.strip() for c in stripped.split("|")[1:-1]]
        if len(cells) < 20:
            in_table = False
            continue

        # Require a DCBM ID in the second column
        pid = cells[1] if len(cells) > 1 else ""
        if not pid or "DCBM" not in pid.upper():
            continue

        # Select field mapping based on cell count
        # 26 cells = Daily Brief missing "埋深/对象深度"
        # 27 cells = full master format
        if len(cells) == 26:
            field_map = MATRIX_FIELDS_26
        elif len(cells) == 27:
            field_map = MASTER_FIELDS_27
        else:
            # Try best-effort with 27-field map, truncating extra cells
            field_map = MASTER_FIELDS_27

        cand: dict[str, Any] = {
            "provisional_id": pid,
            "recommendation": "入库",
            "doi": "",
            "title_en": "",
            "title_zh": "",
            "first_author": "",
            "authors": "",
            "year": "",
            "journal": "",
            "volume": "",
            "issue": "",
            "pages_or_article": "",
            "official_url": "",
            "document_type": "",
            "study_area": "",
            "research_object": "",
            "burial_depth": "",
            "research_purpose": "",
            "methods": "",
            "findings": "",
            "innovation": "",
            "limitations": "",
            "relevance": "",
            "suggested_chapter": "",
            "tags": "",
            "reading_priority": "",
            "verification_status": "",
            "ris": "",
            "bibtex": "",
        }

        for idx, field_name in field_map:
            if idx < len(cells) and cells[idx] not in SKIP_VALUES:
                cand[field_name] = cells[idx]

        # Normalize: strip provisional suffix from ID for cleaner logging
        pid_clean = re.sub(r"\s*\(?provisional\)?\s*", "", pid, flags=re.IGNORECASE).strip()
        cand["provisional_id"] = pid_clean

        candidates.append(cand)

    return candidates


def _split_ris_entries(text: str) -> list[str]:
    """Split RIS fenced block into per-record entries on ER  - lines."""
    # Find RIS fence
    m = re.search(r"```ris\s*\n(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    body = m.group(1)
    entries: list[str] = []
    current: list[str] = []
    for line in body.split("\n"):
        if line.strip().startswith("ER ") or line.strip() == "ER  -":
            if current:
                entries.append("\n".join(current))
                current = []
        current.append(line)
    if current:
        entries.append("\n".join(current))
    return entries


def _split_bibtex_entries(text: str) -> list[str]:
    """Split BibTeX fenced block into per-record entries."""
    m = re.search(r"```bibtex\s*\n(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    body = m.group(1)
    # Split on @article boundaries
    entries = []
    current: list[str] = []
    for line in body.split("\n"):
        if line.strip().startswith("@article{") and current:
            entries.append("\n".join(current))
            current = []
        current.append(line)
    if current:
        entries.append("\n".join(current))
    return entries
