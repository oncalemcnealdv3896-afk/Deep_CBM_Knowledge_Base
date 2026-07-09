# Deep CBM Knowledge Base

Deep CBM Knowledge Base is a continuously curated, version-controlled, evidence-based research knowledge system for deep coalbed methane, deep CBM, and coal-rock gas literature.

本仓库用于长期维护深部煤层气、深部 CBM、深部煤岩气相关文献知识库。它不是普通文献列表，而是一个版本可追溯、持续更新、面向博士论文和科研写作的知识系统。

## Current Baseline

- 当前基准文件：`00_Master/Deep_CBM_Latest.xlsx`
- 原始来源文件：`00_Master/source/Deep_CBM_complete_literature_matrix_v1_105.xlsx`
- 当前初始化日期：`2026-07-09`
- 当前候选总数：118
- 第一张 sheet 必须为：`完整文献矩阵`

## Update Rules

- GitHub 仓库是唯一真源 Single Source of Truth。
- 每日更新必须保留所有原有 sheet、格式、公式、超链接和用户手工维护内容。
- 不得删除任何已有数据文件。
- 不得覆盖用户手工维护内容。
- 不得重建简化版 Excel。
- 如需修改 Excel，必须保留所有原有 sheet、格式、公式、超链接和批注。
- `08_User` 是用户个人研究区，不得被自动覆盖。

## Deduplication Order

1. DOI
2. 英文题名
3. 中文题名
4. 第一作者 + 年份
5. 人工核查
## Daily Brief Workflow

Daily literature updates are driven by Markdown briefs.

ChatGPT generates daily briefs under:

09_Daily_Brief/YYYY-MM-DD/Deep_CBM_daily_brief_YYYYMMDD.md

Codex reads each daily brief and then updates the Excel master workbook, snapshots, increment files, RIS/BibTeX exports, QC reports, and changelog.

ChatGPT must not directly edit 00_Master/Deep_CBM_Latest.xlsx.

User personal markings and reading notes must be saved only under 08_User/.

The daily brief is the source of truth for each daily update. Codex must not update the master workbook based only on chat history.
## Master Index for ChatGPT Deduplication

ChatGPT reads the GitHub repository as the source of truth for daily literature deduplication.

To make deduplication reliable, Codex exports machine-readable index files from the master workbook:

- 00_Master/index/Deep_CBM_master_index.csv
- 00_Master/index/Deep_CBM_master_index.jsonl

These files are regenerated after every update to 00_Master/Deep_CBM_Latest.xlsx.

ChatGPT uses these index files to check:
- DOI duplication
- English title duplication
- Chinese title duplication
- author-year similarity

The Excel workbook remains the master human-readable database, but the index files are the preferred machine-readable deduplication source.
