# Master Index

This directory stores machine-readable index files exported from the first worksheet `完整文献矩阵` of `00_Master/Deep_CBM_Latest.xlsx`.

这些索引用于让 ChatGPT 每天读取 GitHub 仓库后进行 DOI、题名和作者年份去重，而不必直接依赖二进制 Excel 文件。

## Files

- Deep_CBM_master_index.csv  
  CSV index for daily deduplication.

- Deep_CBM_master_index.jsonl  
  JSON Lines index for robust machine reading.

## Required fields

- 文献ID
- DOI
- DOI_normalized
- 英文题名
- 英文题名_normalized
- 中文题名
- 中文题名_normalized
- 第一作者
- 年份
- 期刊/来源
- 官方网页
- 核验状态

## Rule

After every update to `00_Master/Deep_CBM_Latest.xlsx`, Codex must regenerate these index files.