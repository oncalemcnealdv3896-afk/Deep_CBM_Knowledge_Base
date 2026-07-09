# Deep CBM Knowledge Base 使用说明书

## 0. 项目定位

Deep CBM Knowledge Base 是用于长期维护深部煤层气、deep CBM、deep coalbed methane、deep coal-rock gas、深部煤岩气相关文献的科研知识库。

本仓库不是普通 Excel 文献表，而是一个由 GitHub 管理版本、由 ChatGPT 生成每日文献简报、由 Codex 维护主表、由用户进行科研标记的长期知识系统。

核心原则：

1. GitHub 仓库是唯一真源。
2. `00_Master/Deep_CBM_Latest.xlsx` 是唯一最新版主库。
3. ChatGPT 不直接修改 Excel 主表，只生成 Daily Brief。
4. Codex 根据 Daily Brief 更新主表和生成文件。
5. 用户个人阅读笔记和判断只写入 `08_User/`。
6. 每次主表更新后必须重新导出机器可读索引。
7. 任何更新不得破坏原有 sheet、字段、公式、格式、超链接、批注和用户内容。

---

## 1. 每日维护总流程

每日维护分为 5 步。

### Step 1：ChatGPT 读取仓库索引并生成 Daily Brief

ChatGPT 每天优先读取：

* `00_Master/index/Deep_CBM_master_index.csv`
* `00_Master/index/Deep_CBM_master_index.jsonl`

然后检索当天可能新增或正式发表的深部煤层气文献，按 DOI、英文题名、中文题名、第一作者+年份查重。

如果发现新增文献，ChatGPT 生成：

* `09_Daily_Brief/YYYY-MM-DD/Deep_CBM_daily_brief_YYYYMMDD.md`

如果没有新增文献，默认不通知用户。

### Step 2：用户阅读 Daily Brief

用户每天像阅读晨报一样阅读：

* `09_Daily_Brief/YYYY-MM-DD/Deep_CBM_daily_brief_YYYYMMDD.md`

重点看：

* 今日是否有新增文献；
* 哪些文献值得精读；
* 哪些文献与博士课题相关；
* 哪些文献适合写进综述、讨论或方法章节；
* 是否有新的研究空白或趋势。

### Step 3：用户做个人标记

用户自己的判断、阅读计划、灵感和论文使用记录只写入：

* `08_User/`

推荐文件：

* `08_User/Reading_Marks_YYYYMMDD.md`
* `08_User/Research_Ideas.md`
* `08_User/Chapter_Citation_Map.md`
* `08_User/My_Reading_Plan.md`

不要把个人判断直接写进系统维护区，例如 `00_Master/`、`01_Increment/`、`02_RIS/`、`06_Statistics/`。

### Step 4：Codex 根据 Daily Brief 更新主库

Codex 读取当天 Daily Brief 后更新：

* `00_Master/Deep_CBM_Latest.xlsx`
* `00_Master/snapshots/`
* `01_Increment/YYYY-MM-DD/`
* `02_RIS/`
* `03_BibTeX/`
* `06_Statistics/`
* `CHANGELOG.md`
* `00_Master/index/`

Codex 必须在更新完成后运行：

* `python scripts/export_master_index.py`

或：

* `py scripts/export_master_index.py`

以重新生成机器可读索引。

### Step 5：提交并推送 GitHub

Codex 或用户完成验证后提交：

* `git add .`
* `git commit -m "update: refresh Deep CBM Knowledge Base YYYY-MM-DD"`
* `git push`

---

## 2. 仓库目录说明

### 根目录

根目录保存项目级文件。

包括：

* `README.md`
* `USER_MANUAL.md`
* `CHANGELOG.md`
* `CONTRIBUTING.md`
* `LICENSE`
* `.gitignore`

#### README.md

项目首页说明。用于快速介绍项目目的、当前主库、更新规则和目录结构。

#### USER_MANUAL.md

本使用说明书。用于详细说明整个仓库如何维护、每个目录放什么、用户和 Codex 应该怎么操作。

#### CHANGELOG.md

变更日志。每次主库更新、脚本更新、结构调整、QC 修复都必须记录。

每条日志应说明：

* 日期；
* 更新来源；
* 新增文献编号；
* 是否更新主表；
* 是否生成快照；
* 是否更新索引；
* 是否有异常或人工复核项。

#### CONTRIBUTING.md

贡献和维护规范。Codex 每次执行任务前应遵守其中规则。

#### LICENSE

项目许可证。注意：许可证只覆盖仓库中你有权发布的材料，不自动覆盖出版社 PDF 或第三方版权材料。

#### .gitignore

忽略本地临时文件、日志、缓存、Excel 锁文件等。

必须忽略：

* `_local_logs/`
* `_incoming_*/`
* `~$*.xlsx`
* `*.tmp`
* `*.bak`
* `.DS_Store`
* `Thumbs.db`

如果仓库保持 public，建议默认不要提交出版社 PDF。

---

## 3. 00_Master：主库区

路径：

* `00_Master/`

这是整个知识库最核心的目录。

### 00_Master/Deep_CBM_Latest.xlsx

唯一最新版 Excel 主库。

规则：

1. 第一张 sheet 必须叫 `完整文献矩阵`。
2. 第一张 sheet 必须是最新版完整文献总表。
3. 所有新增文献必须追加到第一张 sheet。
4. 不得删除原有 sheet。
5. 不得破坏格式、公式、筛选、超链接、批注。
6. 不得用简化版 Excel 覆盖此文件。

这个文件由 Codex 维护，不建议用户手动批量修改。

用户可以查看，但个人判断不要直接写在这里，除非你明确决定该字段属于主库字段。

### 00_Master/source/

保存原始基准文件。

当前包括：

* `Deep_CBM_complete_literature_matrix_v1_105.xlsx`

这个目录用于保留历史原始输入，不应修改。

### 00_Master/snapshots/

保存每日完整快照。

命名规则：

* `Deep_CBM_Knowledge_Base_YYYY-MM-DD.xlsx`

例如：

* `Deep_CBM_Knowledge_Base_2026-07-09.xlsx`

用途：

* 回滚；
* 历史追踪；
* 证明某一天数据库状态；
* 论文写作时引用某一版本。

快照只追加，不删除。

### 00_Master/index/

保存机器可读索引。

包括：

* `Deep_CBM_master_index.csv`
* `Deep_CBM_master_index.jsonl`
* `README.md`

用途：

* 给 ChatGPT 查重；
* 给 Codex 自动检查；
* 避免每天依赖二进制 Excel；
* 支持 DOI、题名、作者年份去重。

每次更新 `Deep_CBM_Latest.xlsx` 后，必须重新运行：

* `python scripts/export_master_index.py`

或：

* `py scripts/export_master_index.py`

---

## 4. 01_Increment：每日增量区

路径：

* `01_Increment/YYYY-MM-DD/`

每一天有一个文件夹。

例如：

* `01_Increment/2026-07-09/`

里面保存当天新增文献和更新记录。

推荐文件：

* `Deep_CBM_increment_YYYYMMDD.xlsx`
* `Deep_CBM_increment_YYYYMMDD.ris`
* `Deep_CBM_increment_YYYYMMDD.bib`
* `Deep_CBM_update_log_YYYYMMDD.md`
* `Deep_CBM_duplicate_check_YYYYMMDD.xlsx`

### Deep_CBM_increment_YYYYMMDD.xlsx

只包含当天新增文献。

字段应与主表一致。

### Deep_CBM_increment_YYYYMMDD.ris

当天新增文献的 RIS 文件，可导入 Zotero、EndNote、NoteExpress。

### Deep_CBM_increment_YYYYMMDD.bib

当天新增文献的 BibTeX 文件。如果当天没有生成 BibTeX，需要在 QC 报告中说明。

### Deep_CBM_update_log_YYYYMMDD.md

当天更新日志，说明新增、跳过、重复、修复、人工复核项。

### Deep_CBM_duplicate_check_YYYYMMDD.xlsx

当天查重报告，记录 DOI、题名、作者年份判断。

---

## 5. 02_RIS：RIS 管理区

路径：

* `02_RIS/`

保存 RIS 文件。

### 02_RIS/Deep_CBM_complete.ris

完整知识库的 RIS 文件。

如果脚本支持，应在每次主表更新后重新生成。

### 02_RIS/increment/

保存每日增量 RIS。

命名规则：

* `Deep_CBM_increment_YYYYMMDD.ris`

---

## 6. 03_BibTeX：BibTeX 管理区

路径：

* `03_BibTeX/`

保存 BibTeX 文件。

### 03_BibTeX/Deep_CBM_complete.bib

完整知识库的 BibTeX 文件。如果当前还没有，可以后续由 Codex 脚本生成。

### 03_BibTeX/increment/

保存每日增量 BibTeX。

命名规则：

* `Deep_CBM_increment_YYYYMMDD.bib`

如果当天没有 BibTeX，不强制失败，但应在 QC 报告中说明。

---

## 7. 04_PDF：PDF 与附件区

路径：

* `04_PDF/`

此目录目前可以为空。它的用途不是强制收集所有 PDF，而是管理你有权保存的全文、补充材料和附件索引。

### 重要版权原则

如果仓库是 public，不建议直接提交出版社 PDF，除非它明确是开放获取并允许再分发。

推荐规则：

1. 开放获取 PDF 可以保存，但要记录来源和授权。
2. 非开放获取 PDF 不要提交到 GitHub。
3. 学校数据库下载的个人阅读 PDF 可以保存在本地 Zotero、OneDrive 或电脑目录，但不建议推送到 public GitHub。
4. 对于不能上传的 PDF，只在仓库中保存元数据和本地位置说明。

### 推荐子目录

可以让 Codex 后续创建：

* `04_PDF/README.md`
* `04_PDF/PDF_Index.csv`
* `04_PDF/open_access/`
* `04_PDF/supplementary/`
* `04_PDF/metadata_only/`

### PDF_Index.csv 推荐字段

* 文献ID
* DOI
* 题名
* PDF状态
* PDF来源URL
* 授权类型
* 本地保存位置
* 是否可提交GitHub
* 备注

### PDF 文件命名建议

如果 PDF 可以合法保存，推荐命名：

* `DCBM-001_TAO_2026_JCCS.pdf`
* `DCBM-088_YANG_2026_productivity_prediction.pdf`

命名规则：

* 以文献ID开头；
* 包含第一作者；
* 包含年份；
* 包含简短题名；
* 不使用中文空格和特殊符号。

### metadata_only 的用途

如果不能上传 PDF，可在 `metadata_only/` 中保存一个 Markdown 说明：

* `DCBM-001_pdf_note.md`

内容包括：

* DOI；
* 官方网页；
* PDF 获取方式；
* 是否已本地保存；
* 本地保存在哪里；
* 是否有补充材料。

---

## 8. 05_Summaries：文献精读卡区

路径：

* `05_Summaries/`

用于保存每篇文献的 Markdown 精读卡。

命名规则：

* `DCBM-001.md`
* `DCBM-002.md`
* `DCBM-121.md`

每篇精读卡建议包括：

1. 基本信息；
2. 一句话总结；
3. 研究区；
4. 研究对象；
5. 数据来源；
6. 方法；
7. 核心发现；
8. 创新点；
9. 局限性；
10. 与博士课题关系；
11. 建议引用章节；
12. 精读优先级；
13. 个人备注链接。

### 谁维护？

ChatGPT 可根据文献内容生成草稿。

Codex 可把草稿保存为 Markdown 文件。

用户可在 `08_User/` 中做个人评价，不建议直接覆盖系统精读卡，除非是正式修订。

---

## 9. 06_Statistics：统计与质量控制区

路径：

* `06_Statistics/`

用于保存统计表、QC 报告、图表和校验报告。

当前包括：

* `Initial_Validation_Report_20260709.md`
* `Master_Index_Report_20260709.md`
* `README.md`

推荐后续文件：

* `QC_Report_YYYYMMDD.md`
* `Statistics_YYYYMMDD.xlsx`
* `Topic_Distribution_YYYYMMDD.csv`
* `Journal_Distribution_YYYYMMDD.csv`
* `Year_Distribution_YYYYMMDD.csv`

每次主表更新后，至少应生成：

* `QC_Report_YYYYMMDD.md`

QC 报告应检查：

1. 第一张 sheet 是否为 `完整文献矩阵`；
2. 文献ID是否连续；
3. DOI是否重复；
4. 英文题名是否重复；
5. 中文题名是否重复；
6. 原有 sheet 是否保留；
7. 是否修改 `08_User/`；
8. 是否生成快照；
9. 是否更新索引；
10. 是否有人工复核项。

---

## 10. 07_Knowledge：知识层区

路径：

* `07_Knowledge/`

这个目录不是放题录，而是放从文献中提炼出来的知识。

推荐文件：

* `Reservoir.md`
* `Fracturing.md`
* `Production.md`
* `Geology.md`
* `MachineLearning.md`
* `ResponsePattern.md`
* `Research_Gap.md`
* `Evidence_Matrix.md`
* `Contradiction_Matrix.md`

### Reservoir.md

保存储层相关知识，例如：

* 孔隙结构；
* 吸附/解吸；
* 渗透率；
* 储层非均质性；
* 煤阶；
* 含气性。

### Fracturing.md

保存压裂相关知识，例如：

* 体积压裂；
* 水力裂缝扩展；
* 地应力；
* CO2 预强化；
* 裂缝监测；
* 甜点段。

### Production.md

保存开发与排采相关知识，例如：

* 排采制度；
* 焖井；
* 控压排采；
* 返排；
* 产能预测；
* 全生命周期动态。

### ResponsePattern.md

与你的博士课题高度相关，建议重点维护。

可保存：

* 早期响应；
* 排采曲线；
* response classification；
* early gas response；
* production behavior；
* 动态数据特征。

### Evidence_Matrix.md

用于记录“某个结论由哪些文献支持”。

例如：

* 深部煤层气开发初期游离气贡献高：DCBM-XXX、DCBM-YYY。
* 地应力控制裂缝形态：DCBM-AAA、DCBM-BBB。

### Contradiction_Matrix.md

用于记录文献之间的矛盾。

例如：

* 有文献认为高地应力有利于裂缝复杂性；
* 另一类文献认为高地应力抑制裂缝扩展；
* 原因可能是研究区、煤阶、埋深和压裂工艺不同。

### Research_Gap.md

用于持续记录研究空白。

这是服务你博士论文最重要的文件之一。

---

## 11. 08_User：用户个人研究区

路径：

* `08_User/`

这是用户自己的区域，任何自动流程不得覆盖。

推荐文件：

* `Reading_Marks_YYYYMMDD.md`
* `Research_Ideas.md`
* `Chapter_Citation_Map.md`
* `My_Reading_Plan.md`
* `Paper_Draft_Links.md`
* `Personal_Notes.md`

### Reading_Marks_YYYYMMDD.md

每天读完 Daily Brief 后，记录个人判断。

示例：

# Reading Marks - 2026-07-09

## DCBM-121

* 个人判断：必读
* 用途：第四章讨论、第五章产能解释
* 与课题关系：强
* 备注：可用于解释深部煤层气水平井全生命周期产能变化

### Research_Ideas.md

保存科研灵感。

例如：

* 是否可以用早期排采曲线预测后期产能；
* 是否能建立 response classification；
* 是否可把返排特征与压裂效果联系起来。

### Chapter_Citation_Map.md

记录每篇文献适合放在论文哪一章。

例如：

* 第二章文献综述：DCBM-001、DCBM-002、DCBM-114。
* 第四章结果讨论：DCBM-088、DCBM-121。
* 第五章机制分析：DCBM-108、DCBM-109。

---

## 12. 09_Daily_Brief：每日简报区

路径：

* `09_Daily_Brief/`

用于保存 ChatGPT 每天生成的 Markdown 简报。

路径规则：

* `09_Daily_Brief/YYYY-MM-DD/Deep_CBM_daily_brief_YYYYMMDD.md`

例如：

* `09_Daily_Brief/2026-07-09/Deep_CBM_daily_brief_20260709.md`

Daily Brief 是 Codex 每天更新主表的唯一依据。

Daily Brief 应包括：

1. 今日结论；
2. 检索范围；
3. 新增候选文献；
4. DOI/URL 核验；
5. 去重依据；
6. 推荐 DCBM 编号；
7. 详细中文说明；
8. 可写入主表的矩阵行；
9. RIS 增量；
10. BibTeX 增量；
11. 给 Codex 的维护指令；
12. 给用户的阅读建议。

如果没有新增文献，可以不生成通知，也可以生成 no-update 简报用于记录，视用户需求决定。

---

## 13. scripts：脚本区

路径：

* `scripts/`

用于保存自动化脚本。

当前重要脚本：

* `export_master_index.py`

### export_master_index.py

用途：

从 `00_Master/Deep_CBM_Latest.xlsx` 第一张 sheet `完整文献矩阵` 中导出机器可读索引。

输出：

* `00_Master/index/Deep_CBM_master_index.csv`
* `00_Master/index/Deep_CBM_master_index.jsonl`
* `06_Statistics/Master_Index_Report_YYYYMMDD.md`

运行方式：

* `python scripts/export_master_index.py`

或：

* `py scripts/export_master_index.py`

每次主表更新后必须运行。

后续可增加脚本：

* `update_ris.py`
* `update_bibtex.py`
* `validate_master_workbook.py`
* `generate_statistics.py`
* `create_daily_snapshot.py`

---

## 14. PDF 维护建议

PDF 目录目前为空是正常的，不需要着急填满。

推荐策略：

### 如果仓库是 public

不要直接提交出版社 PDF。

只维护：

* PDF_Index.csv；
* 开放获取 PDF 的链接；
* 本地保存路径；
* 是否已下载；
* 是否可公开。

### 如果仓库改为 private

仍建议谨慎处理 PDF。学校数据库下载的 PDF 通常只适合个人阅读，不建议再分发。

### 最推荐方式

把 PDF 放在本地 Zotero 或本地硬盘，仓库只保存索引。

例如：

* 本地 Zotero 保存全文；
* GitHub 保存 DOI、URL、Zotero Key、本地位置；
* 对开放获取的文献可记录 PDF URL。

### PDF_Index.csv 示例字段

文献ID, DOI, 题名, PDF状态, PDF来源URL, 授权类型, 本地保存位置, 是否可提交GitHub, 备注

PDF状态可选：

* not_collected
* local_only
* open_access_url_only
* open_access_pdf_saved
* supplementary_saved
* unavailable

---

## 15. 用户每日操作指南

### 早上

用户对 ChatGPT 说：

生成今天的 Deep CBM Daily Brief

ChatGPT 读取 GitHub 索引并检索新文献。

### 读简报

阅读：

* `09_Daily_Brief/YYYY-MM-DD/Deep_CBM_daily_brief_YYYYMMDD.md`

### 写个人标记

写入：

* `08_User/Reading_Marks_YYYYMMDD.md`

### 交给 Codex 更新主库

给 Codex 的日常指令：

请先 git pull，然后读取今天的 Daily Brief，按其中指令更新 Deep_CBM_Latest.xlsx 和相关文件；更新完成后运行 scripts/export_master_index.py 重新生成 master index，生成 QC 报告，确认 08_User 未被自动修改，最后 git commit 并 push。

---

## 16. Codex 每日维护检查清单

Codex 每日更新时必须检查：

1. 是否先执行 `git pull`；
2. 是否读取当天 Daily Brief；
3. 是否基于现有 Excel 修改，而不是重建 Excel；
4. 第一张 sheet 是否仍为 `完整文献矩阵`；
5. 文献ID是否连续；
6. DOI是否重复；
7. 英文题名是否重复；
8. 中文题名是否重复；
9. 原有 sheet 是否保留；
10. `08_User/` 是否未被自动修改；
11. 是否生成当天快照；
12. 是否生成当天增量 Excel；
13. 是否生成 RIS；
14. 是否生成 BibTeX；
15. 是否生成 QC 报告；
16. 是否运行 `scripts/export_master_index.py`；
17. 是否更新 `Deep_CBM_master_index.csv/jsonl`；
18. 是否更新 `CHANGELOG.md`；
19. 是否 commit；
20. 是否 push。

---

## 17. 今天的演练方式

今天不需要修改主表。

今天演练建议只做三件事：

1. 新增 `USER_MANUAL.md`；
2. 可选新增 `09_Daily_Brief/2026-07-09/Deep_CBM_daily_brief_20260709_REHEARSAL.md`；
3. Codex 提交并推送。

演练版 Daily Brief 可以写明：

* 今日为流程演练；
* 不新增文献；
* 不修改主表；
* 不生成增量文件；
* 不改变 `00_Master/Deep_CBM_Latest.xlsx`；
* 仅验证 Daily Brief 工作流可用。

---

## 18. 最重要的原则

永远记住：

* Excel 是主库；
* GitHub 是唯一真源；
* Index 是机器查重入口；
* Daily Brief 是每日更新依据；
* `08_User/` 是用户个人研究区；
* Codex 负责工程维护；
* ChatGPT 负责文献检索和知识组织；
* 用户负责科研判断。

这个仓库的目标不是保存文件，而是长期支撑博士论文、综述写作和深部煤层气研究。
