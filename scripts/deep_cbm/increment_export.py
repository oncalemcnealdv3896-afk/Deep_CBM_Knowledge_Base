"""Increment exporter — generate daily increment Excel, RIS, BibTeX, and logs."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

from openpyxl import Workbook

ROOT = Path(__file__).resolve().parents[2]
INCREMENT_DIR = ROOT / "01_Increment"
RIS_DIR = ROOT / "02_RIS" / "increment"
BIB_DIR = ROOT / "03_BibTeX" / "increment"

MASTER_COLUMNS = [
    "序号", "文献ID", "第一作者", "全部作者", "年份", "英文题名", "中文题名",
    "期刊/来源", "卷", "期", "页码/文章号", "DOI", "官方网页", "文献类型",
    "研究区域/区块", "研究对象", "埋深/对象深度", "研究目的", "主要方法",
    "核心结论", "创新点", "局限性", "与你课题的关联", "建议引用章节",
    "关键词/标签", "精读优先级", "核验状态",
]


def export_increment(
    candidates: list[dict[str, Any]],
    proposed_ids: list[str],
    duplicate_log: list[dict[str, Any]],
    run_dir: Path,
) -> dict[str, Any]:
    """Generate all increment files. Returns paths dict."""
    today = date.today().strftime("%Y%m%d")
    today_dash = date.today().isoformat()
    inc_dir = INCREMENT_DIR / f"{today_dash}_daily_brief_update"
    inc_dir.mkdir(parents=True, exist_ok=True)
    RIS_DIR.mkdir(parents=True, exist_ok=True)
    BIB_DIR.mkdir(parents=True, exist_ok=True)

    results: dict[str, str] = {}

    # ---- Increment Excel ---------------------------------------------------
    inc_xlsx = inc_dir / f"Deep_CBM_increment_{today}.xlsx"
    _write_increment_xlsx(candidates, proposed_ids, inc_xlsx)
    results["increment_xlsx"] = str(inc_xlsx.relative_to(ROOT))

    # ---- Increment RIS -----------------------------------------------------
    inc_ris = RIS_DIR / f"Deep_CBM_increment_{today}.ris"
    ris_content = "\n\n".join(
        c.get("ris", "") for c in candidates if c.get("ris")
    )
    inc_ris.write_text(ris_content, encoding="utf-8")
    results["increment_ris"] = str(inc_ris.relative_to(ROOT))

    # ---- Increment BibTeX --------------------------------------------------
    inc_bib = BIB_DIR / f"Deep_CBM_increment_{today}.bib"
    bib_content = "\n\n".join(
        c.get("bibtex", "") for c in candidates if c.get("bibtex")
    )
    inc_bib.write_text(bib_content, encoding="utf-8")
    results["increment_bibtex"] = str(inc_bib.relative_to(ROOT))

    # ---- Update Log --------------------------------------------------------
    log_path = inc_dir / f"Deep_CBM_update_log_{today}.md"
    log_lines = [
        f"# Deep CBM Update Log — {today_dash}",
        "",
        f"## Summary",
        f"- 新增 {len(candidates)} 篇",
        f"- 跳过重复 {len(duplicate_log)} 篇",
        f"- 新增编号: {', '.join(proposed_ids) if proposed_ids else '无'}",
        "",
    ]
    if candidates:
        log_lines.append("## New Records")
        for c, pid in zip(candidates, proposed_ids):
            log_lines.append(f"- **{pid}**: {c.get('first_author','?')} ({c.get('year','?')}) — {c.get('title_en','?')[:100]}")
        log_lines.append("")
    if duplicate_log:
        log_lines.append("## Duplicates Skipped")
        for d in duplicate_log:
            log_lines.append(
                f"- Provisional {d.get('provisional_id','?')}: "
                f"{d.get('duplicate_reason','?')} → existing {d.get('existing_dcbm_id','?')}"
            )
        log_lines.append("")
    log_path.write_text("\n".join(log_lines), encoding="utf-8")
    results["update_log"] = str(log_path.relative_to(ROOT))

    # ---- Duplicate Check XLSX ----------------------------------------------
    if duplicate_log:
        dup_path = inc_dir / f"Deep_CBM_duplicate_check_{today}.xlsx"
        _write_duplicate_xlsx(duplicate_log, dup_path)
        results["duplicate_check_xlsx"] = str(dup_path.relative_to(ROOT))

    return results


def _write_increment_xlsx(
    candidates: list[dict[str, Any]], proposed_ids: list[str], path: Path
) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "完整文献矩阵"
    ws.append(MASTER_COLUMNS)

    for i, (cand, final_id) in enumerate(zip(candidates, proposed_ids)):
        ws.append([
            i + 1,
            final_id,
            cand.get("first_author", ""),
            cand.get("authors", ""),
            cand.get("year", ""),
            cand.get("title_en", ""),
            cand.get("title_zh", ""),
            cand.get("journal", ""),
            cand.get("volume", ""),
            cand.get("issue", ""),
            cand.get("pages_or_article", ""),
            cand.get("doi", ""),
            cand.get("official_url", ""),
            cand.get("document_type", ""),
            cand.get("study_area", ""),
            cand.get("research_object", ""),
            cand.get("burial_depth", ""),
            cand.get("research_purpose", ""),
            cand.get("methods", ""),
            cand.get("findings", ""),
            cand.get("innovation", ""),
            cand.get("limitations", ""),
            cand.get("relevance", ""),
            cand.get("suggested_chapter", ""),
            cand.get("tags", ""),
            cand.get("reading_priority", ""),
            cand.get("verification_status", ""),
        ])
    wb.save(str(path))
    wb.close()


def _write_duplicate_xlsx(duplicate_log: list[dict[str, Any]], path: Path) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "重复检查"
    ws.append(["候选原编号", "候选来源/DOI", "判断", "日期", "对应主库ID", "处理"])
    for entry in duplicate_log:
        ws.append([
            entry.get("provisional_id", ""),
            entry.get("existing_doi", ""),
            entry.get("duplicate_reason", ""),
            date.today().isoformat(),
            entry.get("existing_dcbm_id", ""),
            "已跳过",
        ])
    wb.save(str(path))
    wb.close()
