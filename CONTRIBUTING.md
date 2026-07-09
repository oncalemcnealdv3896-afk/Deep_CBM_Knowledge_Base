# Contributing

1. `00_Master/Deep_CBM_Latest.xlsx` 是唯一最新版主库。
2. 每日快照必须放入 `00_Master/snapshots/`。
3. 每日增量必须放入 `01_Increment/YYYY-MM-DD/`。
4. 第一张 sheet 必须是“完整文献矩阵”。
5. 不得删除原有 sheet。
6. 不得删除原有字段。
7. 不得破坏格式、公式、超链接、批注和筛选。
8. `08_User` 是用户个人研究层，任何自动脚本不得覆盖。
9. 新增文献必须先 DOI 去重，再题名去重，再 Author-Year 辅助检查。
10. 每次更新必须修改 `CHANGELOG.md`。
11. 每次更新必须生成或更新 QC 报告。
12. 不得把临时文件、Excel 锁文件、缓存文件提交到 Git。
## Daily Brief Update Rule

Daily updates must follow this order:

1. ChatGPT generates a daily Markdown brief under 09_Daily_Brief/YYYY-MM-DD/.
2. The user reviews the brief and may add personal notes under 08_User/.
3. Codex reads the daily brief and updates the master workbook and generated files.
4. Codex validates that:
   - the first worksheet is 完整文献矩阵;
   - literature IDs are continuous;
   - no existing sheet has been deleted;
   - 08_User/ has not been modified by automation;
   - increment files and QC reports match the daily brief.
5. Codex commits and pushes the update.

Rules:

- Do not update the Excel master workbook without a corresponding Daily Brief.
- Do not use chat history as the update source. Use the saved Daily Brief file as the source of truth for each daily update.
- Do not modify 08_User/ unless the user explicitly asks.
- Do not overwrite user notes.
- Do not delete existing Excel sheets, formulas, hyperlinks, comments, filters, or formatting.
- Every update must be recorded in CHANGELOG.md.
## Master Index Update Rule

After every modification to 00_Master/Deep_CBM_Latest.xlsx, Codex must run:

python scripts/export_master_index.py

or:

py scripts/export_master_index.py

Codex must commit the regenerated files:

- 00_Master/index/Deep_CBM_master_index.csv
- 00_Master/index/Deep_CBM_master_index.jsonl
- 06_Statistics/Master_Index_Report_YYYYMMDD.md

ChatGPT will use these files for daily deduplication.

Do not ask ChatGPT to deduplicate from chat history alone.

## Duplicate Handling Rule

If a Daily Brief contains both duplicate and non-duplicate candidates, Codex must not stop the entire update.

Codex must:
1. Skip duplicate candidates.
2. Record skipped candidates in duplicate check files and update logs.
3. Preserve the existing record ID for duplicated literature.
4. Continue adding non-duplicate candidates.
5. Reassign final DCBM IDs sequentially after the current last ID.
6. Record original suggested ID and final assigned ID.
7. Generate QC reports documenting all skipped and added candidates.
8. Stop only if all candidates are duplicates, or if duplicate status cannot be determined safely.

Do not blindly trust suggested IDs in Daily Brief. Suggested IDs are provisional until checked against the current master workbook and master index.

