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

    # Priority 3: merge Section 5 candidate detail prose (enriches matrix data)
    # If matrix parsing found nothing, create candidates from details alone
    details = _parse_candidate_details(text)
    if details:
        if candidates:
            candidates = _merge_section5_data(candidates, details)
        else:
            candidates = _candidates_from_details(details)
        extraction_method += " + section5"

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

# Compact 10-14 column matrix table
COMPACT_FIELDS = [
    (0, "provisional_id"),
    (1, "recommendation"),
    (2, "doi"),
    (3, "title_en"),
    (4, "first_author"),
    (5, "year"),
    (6, "journal"),
    (7, "pages_or_article"),
    (8, "verification_status"),
    (9, "reading_priority"),
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
        # Support both full (26-27 col) and compact (10 col) table formats
        if len(cells) < 8:
            in_table = False
            continue

        # Require a DCBM ID in the second column
        pid = cells[1] if len(cells) > 1 else ""
        if not pid or "DCBM" not in pid.upper():
            continue

        # Select field mapping based on cell count
        if len(cells) == 26:
            field_map = MATRIX_FIELDS_26
        elif len(cells) == 27:
            field_map = MASTER_FIELDS_27
        elif 8 <= len(cells) <= 14:
            # Compact table (10-14 cols): provisional_id, recommendation, DOI, title_en,
            # first_author, year, journal, vol_issue, verification, priority
            field_map = COMPACT_FIELDS  # type: ignore[assignment]
        else:
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


# ---------------------------------------------------------------------------
# Section 5 candidate detail parser
# ---------------------------------------------------------------------------

def _parse_candidate_details(text: str) -> dict[str, dict[str, str]]:
    """Parse candidate detail blocks (## or ### level, with or without 'provisional')."""
    result: dict[str, dict[str, str]] = {}
    # Match ## or ### DCBM-XXX with optional provisional/MR suffix
    pattern = r"\n(?:###|##)\s+(DCBM-\d+(?:-MR)?)\s*(?:provisional)?\s*\n"
    blocks = re.split(pattern, text)
    for i in range(1, len(blocks), 2):
        pid = blocks[i].strip()
        content = blocks[i + 1] if i + 1 < len(blocks) else ""
        result[pid] = _parse_one_detail(content)
    return result


def _parse_one_detail(text: str) -> dict[str, str]:
    """Parse a single candidate's detail section. Handles both #### subsections
    (old format) and bullet-list narrative (new format)."""
    data: dict[str, str] = {}

    # Try structured #### subsections first (old format)
    basic = _extract_subsection(text, "基本信息")
    if basic:
        data["title_zh_detail"] = _extract_bullet(basic, "建议中文题名")
        data["title_en_detail"] = _extract_bullet(basic, "英文题名")
        data["journal_detail"] = _extract_bullet(basic, "期刊")
        vol_issue = _extract_bullet(basic, "卷期")
        if vol_issue and "(" in vol_issue:
            parts = vol_issue.split("(")
            data["volume_detail"] = parts[0].strip()
            data["issue_detail"] = parts[1].strip().rstrip(")")
        data["pages_detail"] = _extract_bullet(basic, "页码")
        data["doi_detail"] = _extract_bullet(basic, "DOI")
        data["authors_detail"] = _extract_bullet(basic, "作者")

    rp = _extract_subsection(text, "研究对象与研究目的")
    if rp:
        data["research_purpose_detail"] = _clean_prose(rp)
    dm = _extract_subsection(text, "数据与方法")
    if dm:
        data["methods_detail"] = _clean_prose(dm)
    mf = _extract_subsection(text, "主要发现")
    if mf:
        data["findings_detail"] = _clean_prose(mf)
    il = _extract_subsection(text, "创新与局限")
    if il:
        data["innovation_limitations_detail"] = _clean_prose(il)
        innov = _extract_first_sentence_about(il, "创新")
        limit = _extract_first_sentence_about(il, "局限")
        if innov:
            data["innovation_detail"] = innov
        if limit:
            data["limitations_detail"] = limit
    rel = _extract_subsection(text, "与 Deep CBM 研究的关联")
    if rel:
        data["relevance_detail"] = _clean_prose(rel)
    ch = _extract_subsection(text, "建议引用章节")
    if ch:
        data["suggested_chapter_detail"] = _clean_prose(ch)
    rp_match = re.search(r"####\s*阅读优先级\s*\n+(\S+)", text)
    if rp_match:
        priority_raw = rp_match.group(1).strip().strip("*").strip()
        data["reading_priority_detail"] = priority_raw

    # --- Fallback: bullet-list narrative format (new Daily Brief) ---
    if not any(data.values()):
        _parse_narrative_format(text, data)

    return data


def _parse_narrative_format(text: str, data: dict[str, str]) -> None:
    """Parse narrative bullet-point candidate format."""
    # Extract bold title line (Chinese title)
    m = re.search(r'\*\*(.+?)\*\*', text)
    if m:
        data["title_zh_detail"] = m.group(1).strip()

    # Extract English title
    m = re.search(r'(?:英文|English)[：:]\s*\*?(.+?)\*?\s*\n', text)
    if m:
        data["title_en_detail"] = m.group(1).strip()

    # Extract DOI
    m = re.search(r'DOI[：:]\s*`?(10\.\S+?)`?\s*\n', text)
    if not m:
        m = re.search(r'DOI[：:]\s*(10\.\S+)', text)
    if m:
        data["doi_detail"] = m.group(1).strip()

    # Extract journal info: 《Journal》Year, Vol(Issue):Pages
    m = re.search(r'《(.+?)》\s*(\d{4})[,，]\s*(\d+)\((\S+?)\)[：:]\s*(\S+)', text)
    if m:
        data["journal_detail"] = m.group(1).strip()
        data["year_detail"] = m.group(2)
        data["volume_detail"] = m.group(3)
        data["issue_detail"] = m.group(4)
        data["pages_detail"] = m.group(5)

    # Authors: after journal line, before 优先级
    m = re.search(r'(?:作者[：:]|Authors?[：:])\s*(.+?)(?:\n|$)', text, re.IGNORECASE)
    if not m:
        # Try: after English title, before journal
        m = re.search(r'(?:[。；])\s*([A-Z][A-Za-z\s,;.]+?)(?:[\s。；]*《|[\s。；]*DOI|[\s。；]*\*\*优先)', text)
    if m:
        data["authors_detail"] = m.group(1).strip().rstrip(".")

    # Bullet points
    for label, key in [
        ("研究区", "study_area_detail"),
        ("对象", "research_object_detail"),
        ("方法", "methods_detail"),
        ("发现", "findings_detail"),
        ("创新", "innovation_detail"),
        ("局限", "limitations_detail"),
        ("建议引用", "suggested_chapter_detail"),
        ("相关性", "relevance_detail"),
        ("去重", "dedup_note"),
    ]:
        pattern = rf'-\s*{label}[：:]\s*(.+?)(?:\n(?:-\s|$|\n))'
        m = re.search(pattern, text)
        if m:
            data[key] = m.group(1).strip()

    # Priority: **A+** or **A** or **B**
    m = re.search(r'\*\*优先[级别]*[：:]?\s*([A-C][+-]?)\*\*', text)
    if not m:
        m = re.search(r'优先级[：:]\s*\*?\*?\*?([A-C][+-]?)\*?\*?\*?', text)
    if m:
        data["reading_priority_detail"] = m.group(1).strip()

    # Suggested Chinese title
    m = re.search(r'建议中文题名[：:]\s*\*?\*?(.+?)\*?\*?\s*\n', text)
    if m:
        data["title_zh_detail"] = m.group(1).strip()

    # Official URL
    m = re.search(r'(?:官方页|URL)[：:]\s*`?(https?://\S+?)`?\s*\n', text)
    if m:
        data["official_url_detail"] = m.group(1).strip()


def _extract_subsection(text: str, heading: str) -> str | None:
    pattern = rf"####\s+{re.escape(heading)}\s*\n(.*?)(?=\n####|\n---|\n###|\Z)"
    m = re.search(pattern, text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return None


def _extract_bullet(text: str, key: str) -> str:
    pattern = rf"[-*]\s*{re.escape(key)}[：:]\s*(.+?)(?:\n|$)"
    m = re.search(pattern, text)
    if m:
        return m.group(1).strip()
    return ""


def _clean_prose(text: str) -> str:
    text = re.sub(r"^[-*]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _extract_first_sentence_about(text: str, keyword: str) -> str:
    sentences = re.split(r"[。；\n]", text)
    for s in sentences:
        if keyword in s:
            return s.strip()
    return ""


def _merge_section5_data(
    candidates: list[dict[str, Any]], details: dict[str, dict[str, str]]
) -> list[dict[str, Any]]:
    """Merge Section 5 prose into candidate dicts. Table data takes priority."""
    for cand in candidates:
        pid = cand.get("provisional_id", "")
        detail = details.get(pid, {})
        if not detail:
            continue
        _fill_if_empty(cand, "title_zh", detail.get("title_zh_detail", ""))
        _fill_if_empty(cand, "title_en", detail.get("title_en_detail", ""))
        _fill_if_empty(cand, "journal", detail.get("journal_detail", ""))
        _fill_if_empty(cand, "volume", detail.get("volume_detail", ""))
        _fill_if_empty(cand, "issue", detail.get("issue_detail", ""))
        _fill_if_empty(cand, "pages_or_article", detail.get("pages_detail", ""))
        _fill_if_empty(cand, "doi", detail.get("doi_detail", ""))
        _fill_if_empty(cand, "authors", detail.get("authors_detail", ""))
        _fill_if_empty(cand, "year", detail.get("year_detail", ""))
        _fill_if_empty(cand, "study_area", detail.get("study_area_detail", ""))
        _fill_if_empty(cand, "research_object", detail.get("research_object_detail", ""))
        _fill_if_empty(cand, "official_url", detail.get("official_url_detail", ""))
        _enrich_field(cand, "research_purpose", detail.get("research_purpose_detail", ""))
        _enrich_field(cand, "methods", detail.get("methods_detail", ""))
        _enrich_field(cand, "findings", detail.get("findings_detail", ""))
        _enrich_field(cand, "innovation", detail.get("innovation_detail", ""))
        _enrich_field(cand, "limitations", detail.get("limitations_detail", ""))
        _enrich_field(cand, "relevance", detail.get("relevance_detail", ""))
        _enrich_field(cand, "suggested_chapter", detail.get("suggested_chapter_detail", ""))
        if detail.get("reading_priority_detail"):
            cand["reading_priority"] = detail["reading_priority_detail"]
        cand["_detail_prose"] = {
            "research_purpose_prose": detail.get("research_purpose_detail", ""),
            "methods_prose": detail.get("methods_detail", ""),
            "findings_prose": detail.get("findings_detail", ""),
            "innovation_prose": detail.get("innovation_detail", ""),
            "limitations_prose": detail.get("limitations_detail", ""),
            "relevance_prose": detail.get("relevance_detail", ""),
            "suggested_chapter_prose": detail.get("suggested_chapter_detail", ""),
            "innovation_limitations": detail.get("innovation_limitations_detail", ""),
        }
    return candidates


def _candidates_from_details(details: dict[str, dict[str, str]]) -> list[dict[str, Any]]:
    """Create candidate list directly from parsed detail data (when no matrix table)."""
    candidates: list[dict[str, Any]] = []
    for pid, detail in details.items():
        is_mr = "-MR" in pid
        cand: dict[str, Any] = {
            "provisional_id": pid,
            "recommendation": "manual_review_only" if is_mr else "入库",
            "doi": detail.get("doi_detail", ""),
            "title_en": detail.get("title_en_detail", ""),
            "title_zh": detail.get("title_zh_detail", ""),
            "first_author": detail.get("authors_detail", "").split(";")[0].strip() if detail.get("authors_detail") else "",
            "authors": detail.get("authors_detail", ""),
            "year": detail.get("year_detail", ""),
            "journal": detail.get("journal_detail", ""),
            "volume": detail.get("volume_detail", ""),
            "issue": detail.get("issue_detail", ""),
            "pages_or_article": detail.get("pages_detail", ""),
            "official_url": detail.get("official_url_detail", ""),
            "document_type": "",
            "study_area": detail.get("study_area_detail", ""),
            "research_object": detail.get("research_object_detail", ""),
            "burial_depth": "",
            "research_purpose": "",
            "methods": detail.get("methods_detail", ""),
            "findings": detail.get("findings_detail", ""),
            "innovation": detail.get("innovation_detail", ""),
            "limitations": detail.get("limitations_detail", ""),
            "relevance": detail.get("relevance_detail", ""),
            "suggested_chapter": detail.get("suggested_chapter_detail", ""),
            "tags": "",
            "reading_priority": detail.get("reading_priority_detail", ""),
            "verification_status": detail.get("verification_status_detail", ""),
            "ris": "",
            "bibtex": "",
            "_detail_prose": {
                "research_purpose_prose": "",
                "methods_prose": detail.get("methods_detail", ""),
                "findings_prose": detail.get("findings_detail", ""),
                "innovation_prose": detail.get("innovation_detail", ""),
                "limitations_prose": detail.get("limitations_detail", ""),
                "relevance_prose": detail.get("relevance_detail", ""),
                "suggested_chapter_prose": detail.get("suggested_chapter_detail", ""),
                "innovation_limitations": "",
            },
            "dedup_note": detail.get("dedup_note", ""),
        }
        candidates.append(cand)
    return candidates


def _fill_if_empty(cand: dict[str, Any], field: str, value: str) -> None:
    current = cand.get(field, "")
    if not current or current in SKIP_VALUES:
        cand[field] = value


def _enrich_field(cand: dict[str, Any], field: str, prose: str) -> None:
    current = cand.get(field, "")
    if not current or current in SKIP_VALUES:
        cand[field] = prose
    elif prose and len(prose) > len(current) * 1.5:
        cand[field] = prose


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
