# Changelog

## 2026-07-10 Daily Brief Update

- Read and processed Daily Brief: `09_Daily_Brief/2026-07-10/Deep_CBM_daily_brief_20260710.md`
- Added 3 new records: DCBM-122, DCBM-123, DCBM-124 (all from *Petroleum Exploration and Development*, Vol. 53, No. 3, 2026)
- DCBM-122: ZHANG Shuichang — Generation stages and genetic types of coal-rock gas in China
- DCBM-123: LI Guoxin — Formation mechanism of coal-rock gas accumulation transition zones
- DCBM-124: SUN Jinsheng — Cementing and film-forming hydrophobic drilling fluid technology
- Manual review resolved: DCBM-123 (LI Guoxin, 2026) — same author as DCBM-110 but different paper
- No duplicates found; 0 skipped
- Implemented `scripts/daily_ingest.py` deterministic ingestion pipeline (preflight → apply → validate)
- Added `AGENTS.md` with permanent maintenance rules
- Master record count: 121 → 124
- Snapshot: `00_Master/snapshots/Deep_CBM_Knowledge_Base_2026-07-10.xlsx`
- Increment files generated under `01_Increment/2026-07-10_daily_brief_update/`
- Index regenerated under `00_Master/index/`
- QC report: `06_Statistics/QC_Report_20260710_daily_brief_update.md`
- Protected directories (`08_User`, `00_Master/source`, `00_Master/workbook_archive`) unmodified

## 2026-07-09 Workbook Auxiliary Sheet Sync Patch

- Synchronized workbook auxiliary sheets after Daily Brief corrected update.
- Regenerated `网页索引` from the master matrix, now covering DCBM-001 to DCBM-121.
- Updated `总览统计` to the current 121-record state.
- Updated `字段说明` to match all 27 master matrix fields.
- Completed missing `精读摘要` fields for DCBM-119 to DCBM-121.
- Rebuilt workbook internal `QC报告` to remove stale 118-record values.
- Regenerated master index files.
- Did not add new literature records.
- Did not modify `08_User/`, `00_Master/source/`, or `00_Master/workbook_archive/`.

## 2026-07-09 Daily Brief Corrected Update

- Read and corrected Daily Brief: `09_Daily_Brief/2026-07-09/Deep_CBM_daily_brief_20260709.md`
- Skipped duplicate candidate originally proposed as DCBM-119 because DOI `10.3389/feart.2026.1772109` already exists as DCBM-028.
- Added three new records: DCBM-119 to DCBM-121.
- Renumbered non-duplicate candidates from the original Daily Brief:
  - Original DCBM-120 -> DCBM-119
  - Original DCBM-121 -> DCBM-120
  - Original DCBM-122 -> DCBM-121
- Updated master workbook: `00_Master/Deep_CBM_Latest.xlsx`
- Master record count changed from 118 to 121.
- Added snapshot: `00_Master/snapshots/Deep_CBM_Knowledge_Base_2026-07-09_daily_brief_update.xlsx`
- Added increment files under: `01_Increment/2026-07-09_daily_brief_update/`
- Added duplicate check with skipped duplicate reason.
- Regenerated master index files under: `00_Master/index/`
- Generated QC report: `06_Statistics/QC_Report_20260709_daily_brief_update.md`
- Preserved user-maintained files under `08_User/`
- Did not overwrite existing initialization files under `01_Increment/2026-07-09/`

## 2026-07-09

- Cleaned workbook sheet structure for long-term maintenance.
- Preserved active workbook sheets: 完整文献矩阵, 总览统计, 网页索引, 字段说明, 精读摘要, 更新日志, 重复检查, QC报告.
- Archived retired sheets under 00_Master/workbook_archive/2026-07-09_sheet_cleanup/.
- Did not add new literature records.
- Did not modify 08_User/.
- Master workbook remains at 118 records with last ID DCBM-118.

## 2026-07-09

- Initialized GitHub repository structure for Deep CBM Knowledge Base.
- Added original baseline workbook Deep_CBM_complete_literature_matrix_v1_105.xlsx to 00_Master/source/.
- Added current Deep_CBM_Latest.xlsx if available.
- Added 2026-07-09 snapshot if available.
- Added 2026-07-09 increment files if available.
- Added initial validation report.
- Established non-destructive update rule: never delete existing sheets, fields, formulas, hyperlinks, comments, or user-maintained files.
- Confirmed current master workbook contains 118 literature records and the latest first sheet is 完整文献矩阵.
