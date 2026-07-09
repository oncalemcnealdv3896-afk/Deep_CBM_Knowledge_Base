# 09_Daily_Brief

This directory stores daily Markdown briefs generated after each Deep CBM literature watch.

本目录用于存放每日深部煤层气文献简报。每日简报由 ChatGPT 生成，供用户阅读、标记，也供 Codex/Claude Code 后续读取并据此维护 Excel 主表。

## Purpose

ChatGPT does not directly edit the Excel master workbook. Instead, ChatGPT generates a daily Markdown brief containing candidate literature additions, DOI/URL verification, deduplication notes, recommended DCBM IDs, matrix-ready rows, RIS/BibTeX blocks, and explicit update instructions.

Codex reads the daily brief and updates the repository accordingly.

## Daily Brief Path Convention

Daily briefs must be saved under:

09_Daily_Brief/YYYY-MM-DD/Deep_CBM_daily_brief_YYYYMMDD.md

Example:

09_Daily_Brief/2026-07-10/Deep_CBM_daily_brief_20260710.md

## Workflow

1. ChatGPT searches for newly published or newly formalized Deep CBM / deep coalbed methane / coal-rock gas literature.
2. ChatGPT creates a daily Markdown brief under 09_Daily_Brief/YYYY-MM-DD/.
3. The user reads the brief and may add personal comments or markings under 08_User/.
4. Codex reads the daily brief and updates:
   - 00_Master/Deep_CBM_Latest.xlsx
   - 00_Master/snapshots/
   - 01_Increment/YYYY-MM-DD/
   - 02_RIS/
   - 03_BibTeX/
   - 06_Statistics/
   - CHANGELOG.md
5. Codex validates the update.
6. Codex commits and pushes the changes.

## Non-destructive Rules

- Do not edit or delete user-maintained files under 08_User/.
- Do not rebuild a simplified Excel workbook.
- Do not delete existing sheets from Excel.
- Do not delete existing fields from Excel.
- Preserve existing formatting, formulas, hyperlinks, comments, filters, and sheet order as much as possible.
- The first worksheet of 00_Master/Deep_CBM_Latest.xlsx must always be 完整文献矩阵.
- Every update must be traceable through the daily brief, update log, QC report, and Git commit history.