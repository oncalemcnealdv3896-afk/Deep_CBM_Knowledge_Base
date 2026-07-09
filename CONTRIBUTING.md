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
