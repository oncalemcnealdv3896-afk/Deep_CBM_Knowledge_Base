# Deep CBM Knowledge Base Daily Brief — 2026-07-26

> 建议保存路径：`09_Daily_Brief/2026-07-26/Deep_CBM_daily_brief_20260726.md`

## 1. 今日结论

本轮以 GitHub 仓库 `oncalemcnealdv3896-afk/Deep_CBM_Knowledge_Base` 为唯一正式事实来源，重点核对：

- `00_Master/index/Deep_CBM_master_index.jsonl`
- `00_Master/index/Deep_CBM_master_index.csv`
- `06_Statistics/Master_Index_Report_20260724.md`
- `CHANGELOG.md`
- 最近正式处理的 `09_Daily_Brief/2026-07-24/Deep_CBM_daily_brief_20260724.md`

当前正式主库为 **136 条、最后编号 DCBM-136**；文献 ID 连续，DOI、英文题名和中文题名重复数均为 0。最近正式更新为 2026-07-24。

本轮检索日期为 2026-07-26，重点检查 2026-07-24 之后的新发布、正式卷期化记录，并补查近期已正式发表但尚未进入主索引的高相关文献。经 DOI、英文题名、中文题名和第一作者—年份去重，得到：

- **建议 Codex 实时复核后入库：3 篇**
- **人工复核候选：0 篇**
- **未直接修改 Excel、RIS、BibTeX 或 GitHub 仓库**

建议 provisional IDs：

- `DCBM-137`：大宁—吉县区块深部煤层含气量预测模型评价
- `DCBM-138`：织金区块深部煤层气温压吸附行为与预测模型
- `DCBM-139`：测井数据驱动的深部煤层气含量定量评价

以上编号均为 **provisional**。Codex 必须以执行时最新主工作簿和 master index 为准重新查重；如发现重复，应跳过并记录 duplicate reason、matched field 和 existing DCBM ID；其余非重复候选从执行时最后一个实际编号后连续重排。

---

## 2. 当前主库状态

| 项目 | 当前值 |
|---|---:|
| 主工作簿 | `00_Master/Deep_CBM_Latest.xlsx` |
| 总记录数 | 136 |
| 最后编号 | DCBM-136 |
| 文献 ID 连续 | 是 |
| DOI 缺失 | 2 |
| DOI 重复 | 0 |
| 英文题名重复 | 0 |
| 中文题名重复 | 0 |
| 最近正式更新 | 2026-07-24 |

---

## 3. 检索范围与去重方法

### 3.1 检索范围

- `deep coalbed methane`
- `deep coal-rock gas`
- `deep coal seams gas content`
- `pressure-preserved coring`
- `deep CBM temperature pressure adsorption`
- `logging data-driven deep CBM`
- 深部煤层气 含气量
- 深部煤层气 温压吸附
- 深部煤层气 测井预测

### 3.2 去重顺序

1. DOI_normalized 精确匹配；
2. 英文题名_normalized 精确匹配；
3. 中文题名_normalized 精确匹配；
4. 第一作者—年份—题名组合；
5. Online First 与正式卷期版本合并；
6. 最近 Daily Brief 候选交叉检查。

---

# 4. 候选文献

## DCBM-137 provisional

### 基本信息

- 英文题名：**Evaluation of gas content prediction models for deep coal seams: A case study from the Daning–Jixian Block, Eastern Ordos Basin**
- 建议中文题名：**深部煤层含气量预测模型评价：以鄂尔多斯盆地东缘大宁—吉县区块为例**
- 第一作者：Tao Wang
- 作者：Tao Wang; Daojun Huang; Rong Ding; Yimin Cao; Ke Zhou; Guoxiao Zhou; Yunhe Shi; Huaichang Wang; Jianling Hu; Pengfei Jiao; Zongqi Feng; Ze Deng
- 年份：2026
- 期刊：Results in Engineering
- 卷：30
- 文章号：110079
- DOI：`10.1016/j.rineng.2026.110079`
- 官方页面：`https://www.sciencedirect.com/science/article/pii/S2590123026011163`
- 阅读优先级：**A**

### 去重结论

当前 master index 未检出该 DOI或相同中英文题名；第一作者—年份—题名组合亦无匹配，当前判断为非重复候选。

### 研究区、数据与方法

研究区为鄂尔多斯盆地东缘大宁—吉县区块，研究深部煤层中的吸附气、游离气和总含气量。主要采用：

- 保压取心实测含气量；
- 测井资料；
- 高温高压甲烷等温吸附；
- Langmuir 参数、孔隙度和水饱和度预测；
- 吸附气、游离气和总含气量模型；
- 预测结果与保压取心对比。

### 主要发现

- 总含气量约 15.66–35.44 cm³/g；
- 游离气占总含气量约 12.38%–24.30%；
- 吸附气约 4.75–27.3 cm³/g；
- 吸附气占总含气量约 66.42%–84.61%；
- 模型与保压取心实测值总体一致；
- 灰分是影响含气量差异的重要因素。

### 创新、局限与相关性

创新在于将保压取心、测井和高温高压吸附联合，并同时预测吸附气、游离气和总含气量。局限是模型受区块测井响应和煤质特征约束，不能直接外推为长期产能模型。

与用户研究相关性极高，可支撑游离气/吸附气比例、早期游离气贡献、生产动态不能单独反演相态以及后续补充保压取心与测井资料的必要性。

### 建议引用章节

- 引言：深部煤层含气量与相态评价；
- 讨论：游离气和吸附气贡献；
- 局限：动态曲线与储层测试之间的边界；
- 后续研究：测井—取心—吸附联合验证。

---

## DCBM-138 provisional

### 基本信息

- 英文题名：**Adsorption behavior and prediction model of coalbed methane under the influence of temperature and pressure: a case study of the Zhijin Block, Western Guizhou, South China**
- 建议中文题名：**温压影响下煤层气吸附行为与预测模型：以黔西织金区块为例**
- 第一作者：Chen Guo
- 作者：Chen Guo; Lingling Jiang; Lingling Lu; Junzhe Gao; Xi Cheng 等
- 年份：2026
- 期刊：Scientific Reports
- 卷：16
- 文章号：21736
- DOI：`10.1038/s41598-026-52704-3`
- 官方页面：`https://www.nature.com/articles/s41598-026-52704-3`
- 正式发表：2026-05-12
- 阅读优先级：**A−**

### 去重结论

当前 master index 未检出该 DOI或相同中英文题名，当前判断为非重复候选。

### 研究区、数据与方法

研究区为黔西织金区块上二叠统龙潭组。使用来自 4 个向斜、6 个煤矿的 6 件煤样，开展：

- 工业分析、显微组分和镜质体反射率；
- 30、45、60 ℃ 等温吸附；
- 0.1–10 MPa 压力范围；
- 超临界 Langmuir 模型；
- 温度—压力—埋深耦合预测；
- 地温梯度和流体压力梯度分析。

### 主要发现

- 吸附容量随压力升高增加、随温度升高降低；
- 模型拟合 R² 均超过 0.930；
- 吸附气含量随埋深先增后降；
- 6 件样品临界深度约 845–1720 m；
- 区域临界深度约 800–1750 m；
- 固定碳、镜质体反射率和镜质组与吸附能力正相关，惰质组负相关。

### 创新、局限与相关性

创新在于把高阶煤温压吸附实验与区域临界深度预测结合。局限包括样本量仅 6 件，以及该文将 >1000 m 作为深部定义，与主库常见 >1500 m 口径存在差异，不能直接用于用户项目井分类。

适合支撑温压耦合、吸附气—游离气转换、区域深度阈值差异和小样本外推边界。

### 建议引用章节

- 引言：深部温压吸附背景；
- 讨论：吸附气/游离气转换；
- 局限：临界深度和深部定义的区域性。

---

## DCBM-139 provisional

### 基本信息

- 英文题名：**Quantitative Evaluation of Deep Coalbed Methane Content: A Logging Data-Driven Approach**
- 建议中文题名：**测井数据驱动的深部煤层气含量定量评价**
- 第一作者：Yusong Ji
- 作者：Yusong Ji; Song Li; Wei Hou; Yongzhou Li; Peng Feng; Shizhuang Yang; Hanmiao Zhou
- 首次在线：2025-09-21
- 正式卷期：Geological Journal, 2026, 61(7):2072–2086（需 Codex 以 Wiley/Crossref 最终核验）
- DOI：`10.1002/gj.70077`
- 官方页面：`https://onlinelibrary.wiley.com/doi/10.1002/gj.70077`
- 阅读优先级：**A**

### 去重结论

当前 master index 未检出该 DOI或相同中英文题名，当前判断为非重复候选。

### 研究区、数据与方法

研究区为大宁—吉县区块本溪组 8 号煤。主要方法包括：

- 多元回归预测 Langmuir 体积、Langmuir 压力、孔隙度和含水饱和度；
- Langmuir 方程与理想气体状态方程；
- BP 神经网络、多元线性回归、随机森林和支持向量机；
- 压力取心结果验证；
- 测井模型与机器学习模型对比。

### 主要发现

- 传统仅针对吸附气的模型不适用于游离气丰富的深部煤层；
- 测井参数可联合评价吸附气、游离气和总含气量；
- 随机森林在该研究的 4 类机器学习模型中表现最佳；
- 基于物理参数关系的测井模型总体精度高于随机森林；
- 模型在研究区深部段具有较强适应性。

### 创新、局限与相关性

创新在于把测井响应连接到 Langmuir 参数、孔隙度和水饱和度，并比较可解释物理模型与多类机器学习模型。局限是模型受区块标定和压力取心样本约束，且“随机森林最优”仅限该研究候选模型集。

相关性极高，可支撑 feature-specific eligibility、小样本下可解释模型与机器学习边界、游离气/吸附气评价及当前动态数据无法支持正式相态和主控因素结论。

### 建议引用章节

- 引言：深部含气量评价方法；
- 方法讨论：测井与机器学习；
- 讨论：吸附气/游离气；
- 局限：模型可迁移性和资料完整性。

---

# 5. Matrix-ready rows

| provisional_id | recommendation | DOI | 英文题名 | 第一作者 | 年份 | 来源 | 卷期/文章号 | 核验状态 | 优先级 |
|---|---|---|---|---|---:|---|---|---|---|
| DCBM-137 | add_after_live_dedup | 10.1016/j.rineng.2026.110079 | Evaluation of gas content prediction models for deep coal seams | Tao Wang | 2026 | Results in Engineering | 30:110079 | 出版商题名、DOI、卷和文章号已核验 | A |
| DCBM-138 | add_after_live_dedup | 10.1038/s41598-026-52704-3 | Adsorption behavior and prediction model of coalbed methane under temperature and pressure | Chen Guo | 2026 | Scientific Reports | 16:21736 | Nature 官方页和全文已核验 | A− |
| DCBM-139 | add_after_live_dedup | 10.1002/gj.70077 | Quantitative Evaluation of Deep Coalbed Methane Content: A Logging Data-Driven Approach | Yusong Ji | 2025 online / 2026 issue | Geological Journal | 61(7):2072–2086 待最终核验 | Wiley 官方题名、作者、DOI和摘要已核验 | A |

---

# 6. RIS block

```ris
TY  - JOUR
ID  - DCBM-137-PROVISIONAL
AU  - Wang, Tao
AU  - Huang, Daojun
AU  - Ding, Rong
AU  - Cao, Yimin
AU  - Zhou, Ke
AU  - Zhou, Guoxiao
AU  - Shi, Yunhe
AU  - Wang, Huaichang
AU  - Hu, Jianling
AU  - Jiao, Pengfei
AU  - Feng, Zongqi
AU  - Deng, Ze
PY  - 2026
TI  - Evaluation of gas content prediction models for deep coal seams: A case study from the Daning-Jixian Block, Eastern Ordos Basin
T2  - Results in Engineering
VL  - 30
SP  - 110079
DO  - 10.1016/j.rineng.2026.110079
UR  - https://www.sciencedirect.com/science/article/pii/S2590123026011163
N1  - Provisional DCBM ID.
ER  -

TY  - JOUR
ID  - DCBM-138-PROVISIONAL
AU  - Guo, Chen
AU  - Jiang, Lingling
AU  - Lu, Lingling
AU  - Gao, Junzhe
AU  - Cheng, Xi
PY  - 2026
TI  - Adsorption behavior and prediction model of coalbed methane under the influence of temperature and pressure: a case study of the Zhijin Block, Western Guizhou, South China
T2  - Scientific Reports
VL  - 16
SP  - 21736
DO  - 10.1038/s41598-026-52704-3
UR  - https://www.nature.com/articles/s41598-026-52704-3
N1  - Full official author list must be confirmed before import.
ER  -

TY  - JOUR
ID  - DCBM-139-PROVISIONAL
AU  - Ji, Yusong
AU  - Li, Song
AU  - Hou, Wei
AU  - Li, Yongzhou
AU  - Feng, Peng
AU  - Yang, Shizhuang
AU  - Zhou, Hanmiao
PY  - 2026
TI  - Quantitative Evaluation of Deep Coalbed Methane Content: A Logging Data-Driven Approach
T2  - Geological Journal
VL  - 61
IS  - 7
SP  - 2072
EP  - 2086
DO  - 10.1002/gj.70077
UR  - https://onlinelibrary.wiley.com/doi/10.1002/gj.70077
N1  - First published online 2025-09-21; final issue metadata requires verification.
ER  -
```

---

# 7. BibTeX block

```bibtex
@article{Wang2026DeepCoalGasContentModels,
  author={Wang, Tao and Huang, Daojun and Ding, Rong and Cao, Yimin and Zhou, Ke and Zhou, Guoxiao and Shi, Yunhe and Wang, Huaichang and Hu, Jianling and Jiao, Pengfei and Feng, Zongqi and Deng, Ze},
  title={Evaluation of gas content prediction models for deep coal seams: A case study from the Daning--Jixian Block, Eastern Ordos Basin},
  journal={Results in Engineering},
  year={2026}, volume={30}, pages={110079},
  doi={10.1016/j.rineng.2026.110079}
}

@article{Guo2026ZhijinAdsorptionPrediction,
  author={Guo, Chen and Jiang, Lingling and Lu, Lingling and Gao, Junzhe and Cheng, Xi},
  title={Adsorption behavior and prediction model of coalbed methane under the influence of temperature and pressure: a case study of the Zhijin Block, Western Guizhou, South China},
  journal={Scientific Reports},
  year={2026}, volume={16}, pages={21736},
  doi={10.1038/s41598-026-52704-3},
  note={Full official author list requires verification}
}

@article{Ji2026LoggingDeepCBMContent,
  author={Ji, Yusong and Li, Song and Hou, Wei and Li, Yongzhou and Feng, Peng and Yang, Shizhuang and Zhou, Hanmiao},
  title={Quantitative Evaluation of Deep Coalbed Methane Content: A Logging Data-Driven Approach},
  journal={Geological Journal},
  year={2026}, volume={61}, number={7}, pages={2072--2086},
  doi={10.1002/gj.70077},
  note={First published online 2025-09-21; final issue metadata requires verification}
}
```

---

# 8. Codex 执行指令

```text
任务：处理 2026-07-26 Deep CBM Daily Brief。

执行前读取：
1. 00_Master/Deep_CBM_Latest.xlsx
2. 00_Master/index/Deep_CBM_master_index.jsonl
3. 00_Master/index/Deep_CBM_master_index.csv
4. 最新 06_Statistics/Master_Index_Report_*.md
5. CHANGELOG.md
6. 09_Daily_Brief/2026-07-26/Deep_CBM_daily_brief_20260726.md
7. 最近实际存在的 Daily Brief 日期目录

候选 DOI：
- 10.1016/j.rineng.2026.110079
- 10.1038/s41598-026-52704-3
- 10.1002/gj.70077

逐条检查 DOI_normalized、英文题名_normalized、中文题名_normalized、第一作者—年份—题名、Online First/正式卷期和最近 Daily Brief。

发现重复时：
- 跳过；
- 记录 duplicate reason、matched field、existing DCBM ID、DOI和题名；
- 不占用编号；
- 继续处理其余候选。

元数据要求：
- Candidate A：核验全部 12 位作者及 Results in Engineering 30:110079。
- Candidate B：从 Nature/Crossref 获取完整作者；记录 6 件煤样、30/45/60 ℃、0.1–10 MPa；记录 >1000 m 深部口径差异。
- Candidate C：使用 Wiley/Crossref 核验 2026 年卷期页码，同时保留 first published online=2025-09-21。

最终编号：
- DCBM-137—139 均为 provisional；
- 从执行时最后一个实际 ID 后连续编号；
- 重复项不占号、不产生空洞；
- 不修改既有 ID。

正式更新：
1. 更新 Deep_CBM_Latest.xlsx；
2. 保留全部 sheet、格式、公式、超链接、批注和人工内容；
3. 新建 snapshot；
4. 生成 increment Excel、RIS、BibTeX、DOI list；
5. 生成 duplicate check 和 update log；
6. 重建 master index JSONL/CSV；
7. 生成 Master_Index_Report 和 QC report；
8. 更新 CHANGELOG.md。

QC：
- 工作簿可打开；
- 第一张 sheet 为完整文献矩阵；
- 8 个活动 sheet 完整；
- ID连续唯一；
- DOI/英文题名/中文题名重复数均为0；
- 主表、JSONL、CSV数量一致；
- increment 各文件数量一致；
- skipped duplicate含原因和existing ID；
- 作者和卷期核验状态已记录；
- CHANGELOG与实际新增数一致；
- 保护目录未修改。

严格禁止修改：
- 08_User/
- 00_Master/source/
- 00_Master/workbook_archive/
- 历史 snapshots 和 increment
- 用户阅读标记、批注、自定义字段和人工排序
```

---

# 9. Daily ingest manifest

```json
{
  "brief_date": "2026-07-26",
  "brief_type": "candidate_update",
  "repository_source_of_truth_checked": true,
  "master_status_at_check": {
    "record_count": 136,
    "last_id": "DCBM-136",
    "id_continuous": true,
    "doi_missing_count": 2,
    "doi_duplicate_count": 0,
    "english_title_duplicate_count": 0,
    "chinese_title_duplicate_count": 0,
    "last_formal_update": "2026-07-24"
  },
  "recommended_add_count": 3,
  "manual_review_count": 0,
  "provisional_ids": ["DCBM-137", "DCBM-138", "DCBM-139"],
  "codex_action": "preflight_then_apply_verified_nonduplicates_only",
  "direct_repository_edit_performed": false,
  "protected_directory_edit_performed": false
}
```

---

# 10. 最终状态

```text
daily_brief_status: 3_recommended_candidates
repository_source_of_truth_checked: yes
master_record_count_at_check: 136
last_master_id_at_check: DCBM-136
recommended_add_count: 3
manual_review_count: 0
master_workbook_change_needed: pending_codex_live_deduplication
direct_repository_edit_performed: no
protected_directory_edit_performed: no
```
