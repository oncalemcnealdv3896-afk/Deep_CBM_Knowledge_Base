# Deep CBM Knowledge Base Daily Brief — 2026-07-24

> 建议保存路径：`09_Daily_Brief/2026-07-24/Deep_CBM_daily_brief_20260724.md`

## 1. 今日结论

本轮首先读取 GitHub 仓库 `oncalemcnealdv3896-afk/Deep_CBM_Knowledge_Base`，并将以下文件作为唯一正式事实来源：

- `00_Master/index/Deep_CBM_master_index.jsonl`
- `00_Master/index/Deep_CBM_master_index.csv`
- `06_Statistics/Master_Index_Report_20260723.md`
- `CHANGELOG.md`
- `09_Daily_Brief/2026-07-23/Deep_CBM_daily_brief_20260723.md`

当前正式主库状态为：

- 总记录数：**134**
- 最后编号：**DCBM-134**
- 文献 ID 连续：**是**
- DOI 缺失：**2**
- DOI 重复：**0**
- 英文题名重复：**0**
- 中文题名重复：**0**
- 最近正式更新：**2026-07-23**

经 2026-07-23 之后的增量检索，并按 DOI、英文题名、中文题名及第一作者—年份组合进行去重，本轮确认：

- **建议 Codex 执行时再次查重后入库：2 篇**
- **仅人工复核：0 篇**
- **主工作簿需要由 Codex 按正式增量流程更新**
- **未直接修改 Excel、RIS、BibTeX 或 GitHub 仓库**

暂定编号：

- **DCBM-135**：复杂孔隙深部煤层气储层地震岩石物理反演
- **DCBM-136**：华北煤层气藏地球化学演化、微生物控制与生物工程潜力

以上均为 **provisional IDs**。Codex 必须以执行时最新主工作簿和 master index 为准重新查重；如发现重复，应记录 duplicate reason、matched field 和 existing DCBM ID，并对其余非重复候选从执行时最后一个实际编号后连续重新编号。

---

## 2. GitHub 单一事实来源核验

### 2.1 当前正式状态

| 项目 | 当前值 |
|---|---:|
| 主工作簿 | `00_Master/Deep_CBM_Latest.xlsx` |
| 主索引 JSONL | `00_Master/index/Deep_CBM_master_index.jsonl` |
| 主索引 CSV | `00_Master/index/Deep_CBM_master_index.csv` |
| 总记录数 | 134 |
| 最后编号 | DCBM-134 |
| ID 连续 | 是 |
| DOI 缺失 | 2 |
| DOI 重复 | 0 |
| 英文题名重复 | 0 |
| 中文题名重复 | 0 |
| 最近正式更新 | 2026-07-23 |

### 2.2 最近一次正式更新

2026-07-23 正式新增 DCBM-125—DCBM-134，共 10 条；3 条 manual-review 候选因深度边界未入库；5 条已知重复被跳过。主表记录数由 124 增至 134，且保护目录未修改。

### 2.3 当前末端索引

当前 DCBM-125—DCBM-134 已包括：

- 见气时间与排采制度；
- 准噶尔盆地进展；
- 润湿性促解吸；
- 深部吸附热力学；
- 超高盐返排液滑溜水；
- 绥德孔隙多重分形；
- 压裂示踪与机器学习；
- 全域支撑压裂；
- 深部煤层气赋存综述；
- 纳米限域吸附气/游离气评价。

本轮新增候选的 DOI 和题名均未在当前索引中检出。

---

## 3. 检索范围与方法

### 3.1 检索日期与窗口

- 检索日期：**2026-07-24**
- 增量起点：**2026-07-23**
- 扩展范围：近期正式卷期、Online First、未来卷期已完成 DOI 注册或近期被主要数据库发现的高相关文献

### 3.2 检索主题

- deep coalbed methane
- deep CBM
- deep coal-rock gas
- deep coal measures gas
- deep coal reservoir seismic inversion
- deep CBM hydrogeochemistry
- CBM microbiome / microbial methanogenesis
- 深部煤层气地震反演
- 深部煤层气水化学
- 煤层气微生物增产

### 3.3 去重规则

依次检查：

1. DOI_normalized 精确匹配；
2. 英文题名_normalized 精确匹配；
3. 中文题名_normalized 精确匹配；
4. 第一作者—年份—题名组合；
5. Online First、Early Access 和正式卷期合并；
6. 中文版、英文版及数据库重复记录人工核对。

---

# 4. 候选文献

## DCBM-135 provisional

### 基本信息

- 英文题名：**Seismic rock-physics inversion for petrophysical parameters in deep coalbed methane reservoirs with complex pore structures**
- 建议中文题名：**复杂孔隙结构深部煤层气储层岩石物理参数地震反演**
- 第一作者：Qiang Guo
- 作者：Qiang Guo; Yang Chen; Yaping Huang; Jing Ba
- 年份：2026
- 期刊：Journal of Applied Geophysics
- 卷：251
- 文章号：106338
- 正式卷期：2026 年 8 月
- DOI：`10.1016/j.jappgeo.2026.106338`
- 官方页面：`https://www.sciencedirect.com/science/article/abs/pii/S0926985126002478`
- 推荐状态：建议入库
- 阅读优先级：**A−**

### DOI、题名和作者—年份去重

- 当前 master index 未检出该 DOI；
- 未检出相同英文题名；
- 未检出相同中文题名；
- 第一作者 Qiang Guo、2026 与当前末端新增记录无冲突；
- 当前判断：**非重复候选**。

### 研究区与研究对象

研究区位于鄂尔多斯盆地东缘，目标煤层为石炭系本溪组，埋深约 **1500–2300 m**，平均厚度约 **12 m**。研究对象是具有双重孔隙体系和复杂孔隙几何结构的深部煤层气储层。

### 数据与方法

研究构建考虑空间变化孔隙纵横比的岩石物理—地震反演框架，主要包括：

- 两口井测井资料；
- 煤层及围岩岩石物理建模；
- 空间可变孔隙纵横比；
- Taylor 展开线性化正演；
- 高斯混合模型描述多峰岩相统计；
- 贝叶斯线性反演；
- 总孔隙度、黏土体积分数和孔隙纵横比联合预测；
- 鄂尔多斯盆地深部煤层气二维地震剖面验证。

### 主要发现

- 固定孔隙纵横比难以描述深部煤层复杂双孔隙结构；
- 将孔隙纵横比作为空间变化参数可改善储层物性反演；
- 高斯混合先验能够处理煤层及围岩之间的多峰统计分布；
- 反演精度对初始模型和孔隙纵横比敏感；
- 实际二维地震资料应用可辅助识别含气煤层和储层物性变化。

### 创新点

1. 将孔隙几何参数与常规储层物性参数联合反演；
2. 使用空间变化孔隙纵横比表征深部煤层双孔隙复杂性；
3. 将高斯混合统计先验与贝叶斯岩石物理反演结合；
4. 对深部煤层气甜点地震预测提供新的定量参数入口。

### 局限性

- 结果对初始模型和先验信息依赖较高；
- 两口井和单一二维剖面限制了泛化能力；
- 等效孔隙纵横比仍是复杂孔裂隙体系的简化；
- 地震反演只能提供间接储层证据，不能直接证明产气能力；
- 不应将该文反演参数用于用户项目的正式主控因素排序。

### 与用户当前 Deep CBM 研究的相关性

**高。**

可支撑：

- 储层非均质性；
- 裂缝—基质双重孔隙；
- 多源资料和 feature-specific eligibility；
- 为什么仅凭生产曲线不能确定孔隙结构或压裂甜点；
- 后续引入地震、测井和孔裂隙参数的必要性。

### 建议引用章节

- 引言：深部煤储层复杂孔裂隙及预测难点；
- 方法讨论：多源储层参数与地震反演；
- 讨论：储层非均质性作为动态差异的替代解释；
- 局限：间接地球物理证据不能替代生产因果验证。

---

## DCBM-136 provisional

### 基本信息

- 英文题名：**Geochemical evolution and microbial controls on methanogenic potential in North China coalbed methane reservoirs: Implications for CBM bioengineering**
- 建议中文题名：**华北煤层气藏地球化学演化与产甲烷潜力的微生物控制：对煤层气生物工程的启示**
- 第一作者：Q. Zhang
- 作者：Q. Zhang; Y. Li; S. Tang; P. Zhang; S. Zhang; Z. Xi
- 年份：在线元数据 2026；正式卷期 2027
- 期刊：Fuel
- 卷：428，Part C
- 文章号：140384
- 正式卷期日期：2027-01-15
- DOI：`10.1016/j.fuel.2026.140384`
- 官方页面：`https://www.sciencedirect.com/science/article/abs/pii/S0016236126021393`
- 推荐状态：建议入库，需保留 online/formal issue 双重年份说明
- 阅读优先级：**A−**

### DOI、题名和作者—年份去重

- 当前 master index 未检出该 DOI；
- 未检出相同英文题名；
- 未检出相同中文题名；
- 第一作者—年份—题名组合未匹配；
- 当前判断：**非重复候选**。

### 研究区与研究对象

研究覆盖华北 4 个代表性煤层气区：

- 沁水盆地南部；
- 宁武盆地南部；
- 鄂尔多斯盆地东缘神府区块；
- 临兴区块。

研究比较不同埋深、煤阶、水动力条件和保存环境下的气—水—微生物耦合及产甲烷潜力。

### 数据与方法

- 共采样 **69 口生产井**；
- 产出气组分与甲烷碳、氢同位素；
- 产出水主要离子和水化学；
- 溶解无机碳及其同位素；
- 微生物群落；
- 产甲烷功能基因；
- 区域水动力封闭、盐度和水—岩作用对比；
- 沁水南部和神府区块开展更深入微生物分析。

### 主要发现

- 4 个研究区产出气总体以热成因甲烷为主；
- 沁水南部干气特征主要反映高煤阶和高成熟度；
- 沁水南部产出水中存在局部次生微生物改造信号；
- 神府和临兴产出水盐度更高，Na⁺–Cl⁻ 富集和水动力封闭更强；
- 沁水南部具有更高的产甲烷菌多样性和更丰富的产甲烷功能基因；
- 神府区块整体产甲烷功能基因丰度较低，潜力更偏有限的氢营养型路径；
- 水化学条件是限制微生物增产适用性的关键因素。

### 创新点

1. 联合气体、产出水、同位素、微生物群落和功能基因；
2. 在热成因气背景下识别局部次生生物成因改造；
3. 将区域水化学差异与微生物增产适用性直接联系；
4. 为晚期或低产井的微生物增产筛选提供约束框架。

### 局限性

- 微生物深入分析主要集中于沁水南部和神府，区域覆盖并不完全对称；
- 产出水微生物不一定完全代表原位煤基质微生物群落；
- 69 口井均为生产井，长期排采可能已改变原始水化学和微生物状态；
- 产甲烷功能基因表明潜力，不等同于现场增产效果；
- 不宜将微生物机制直接用于解释用户项目的早期动态响应。

### 与用户当前 Deep CBM 研究的相关性

**中高。**

可支撑：

- 产出水化学和水动力封闭；
- 区块差异及保存条件；
- 长期排采后流体环境演化；
- 生物成因与热成因气的区分；
- 用户项目中不能仅凭气水动态推断气源或微生物作用的边界。

### 建议引用章节

- 引言：华北煤层气水化学和气源背景；
- 讨论：产出水、盐度、封闭和区域差异；
- 局限：生产动态不能直接识别气源或微生物机制；
- 展望：低产/晚期井微生物增产的筛选与验证。

---

# 5. Matrix-ready rows

| provisional_id | recommendation | DOI | 英文题名 | 中文题名 | 第一作者 | 年份 | 期刊/来源 | 卷期/文章号 | 官方 URL | 核验状态 | 优先级 |
|---|---|---|---|---|---|---:|---|---|---|---|---|
| DCBM-135 | add_after_live_dedup | 10.1016/j.jappgeo.2026.106338 | Seismic rock-physics inversion for petrophysical parameters in deep coalbed methane reservoirs with complex pore structures | 复杂孔隙结构深部煤层气储层岩石物理参数地震反演 | Qiang Guo | 2026 | Journal of Applied Geophysics | 251:106338 | https://www.sciencedirect.com/science/article/abs/pii/S0926985126002478 | 出版商题名、作者、DOI、卷和文章号已核验 | A− |
| DCBM-136 | add_after_live_dedup | 10.1016/j.fuel.2026.140384 | Geochemical evolution and microbial controls on methanogenic potential in North China coalbed methane reservoirs: Implications for CBM bioengineering | 华北煤层气藏地球化学演化与产甲烷潜力的微生物控制 | Q. Zhang | 2026 online / 2027 issue | Fuel | 428 Part C:140384 | https://www.sciencedirect.com/science/article/abs/pii/S0016236126021393 | 出版商题名、DOI、卷期、摘要和研究设计已核验；作者缩写需 Codex 从 Crossref 补全 | A− |

---

# 6. RIS block

```ris
TY  - JOUR
ID  - DCBM-135-PROVISIONAL
AU  - Guo, Qiang
AU  - Chen, Yang
AU  - Huang, Yaping
AU  - Ba, Jing
PY  - 2026
TI  - Seismic rock-physics inversion for petrophysical parameters in deep coalbed methane reservoirs with complex pore structures
T2  - Journal of Applied Geophysics
VL  - 251
SP  - 106338
DO  - 10.1016/j.jappgeo.2026.106338
UR  - https://www.sciencedirect.com/science/article/abs/pii/S0926985126002478
N1  - Provisional DCBM ID; final ID must be assigned after live master-index deduplication.
ER  -

TY  - JOUR
ID  - DCBM-136-PROVISIONAL
AU  - Zhang, Q.
AU  - Li, Y.
AU  - Tang, S.
AU  - Zhang, P.
AU  - Zhang, S.
AU  - Xi, Z.
PY  - 2027
TI  - Geochemical evolution and microbial controls on methanogenic potential in North China coalbed methane reservoirs: Implications for CBM bioengineering
T2  - Fuel
VL  - 428
IS  - Part C
SP  - 140384
DO  - 10.1016/j.fuel.2026.140384
UR  - https://www.sciencedirect.com/science/article/abs/pii/S0016236126021393
N1  - DOI/online metadata registered in 2026; formal issue dated 2027-01-15. Codex must retrieve full official author names.
N1  - Provisional DCBM ID.
ER  -
```

---

# 7. BibTeX block

```bibtex
@article{Guo2026SeismicRockPhysicsDeepCBM,
  author  = {Guo, Qiang and Chen, Yang and Huang, Yaping and Ba, Jing},
  title   = {Seismic rock-physics inversion for petrophysical parameters in deep coalbed methane reservoirs with complex pore structures},
  journal = {Journal of Applied Geophysics},
  year    = {2026},
  volume  = {251},
  pages   = {106338},
  doi     = {10.1016/j.jappgeo.2026.106338},
  url     = {https://www.sciencedirect.com/science/article/abs/pii/S0926985126002478},
  note    = {Provisional Deep CBM Knowledge Base candidate}
}

@article{Zhang2027NorthChinaCBMMicrobiology,
  author  = {Zhang, Q. and Li, Y. and Tang, S. and Zhang, P. and Zhang, S. and Xi, Z.},
  title   = {Geochemical evolution and microbial controls on methanogenic potential in North China coalbed methane reservoirs: Implications for CBM bioengineering},
  journal = {Fuel},
  year    = {2027},
  volume  = {428},
  pages   = {140384},
  doi     = {10.1016/j.fuel.2026.140384},
  url     = {https://www.sciencedirect.com/science/article/abs/pii/S0016236126021393},
  note    = {Online metadata registered in 2026; formal issue 2027-01-15; full official author names require Crossref verification}
}
```

---

# 8. Codex 执行指令

```text
任务：处理 2026-07-24 Deep CBM Daily Brief。

一、执行前重新读取唯一正式来源

1. 00_Master/Deep_CBM_Latest.xlsx
2. 00_Master/index/Deep_CBM_master_index.jsonl
3. 00_Master/index/Deep_CBM_master_index.csv
4. 最新 06_Statistics/Master_Index_Report_*.md
5. CHANGELOG.md
6. 09_Daily_Brief/2026-07-24/Deep_CBM_daily_brief_20260724.md
7. 最近实际存在的 09_Daily_Brief 日期目录

不得只使用日报中的 master_count=134、last_id=DCBM-134 或 provisional IDs。

二、候选

Candidate A
DOI: 10.1016/j.jappgeo.2026.106338
Title: Seismic rock-physics inversion for petrophysical parameters in deep coalbed methane reservoirs with complex pore structures

Candidate B
DOI: 10.1016/j.fuel.2026.140384
Title: Geochemical evolution and microbial controls on methanogenic potential in North China coalbed methane reservoirs: Implications for CBM bioengineering

三、逐条去重

依次执行：

1. DOI_normalized 精确匹配；
2. 英文题名_normalized 精确匹配；
3. 中文题名_normalized 精确匹配；
4. 第一作者 + 年份 + 严格题名相似性；
5. Online First、Early Access 和正式卷期版本合并检查；
6. 最近 Daily Brief 是否已经推荐同一候选。

如发现重复：

- 跳过该候选；
- 记录 duplicate reason；
- 记录 matched field；
- 记录 existing DCBM ID、DOI及题名；
- 不占用新编号；
- 继续处理其余非重复候选。

四、元数据核验

Candidate A：
- 使用 ScienceDirect 和 Crossref 核验全部作者顺序；
- 核验 volume=251、article=106338；
- 确认 2026 年在线/正式发表日期；
- 记录研究区为鄂尔多斯盆地东缘，煤层埋深约 1500–2300 m。

Candidate B：
- 使用 ScienceDirect 和 Crossref 获取全部作者全名及顺序；
- 核验 DOI、Fuel 428 Part C、article=140384；
- 同时保留 2026 online metadata 和 2027-01-15 formal issue 状态；
- 不得把其错误标为预印本；
- 记录 69 口井样本构成及 4 个研究区；
- 如 Crossref 作者全名仍不完整，更新日志必须保留 metadata limitation。

五、最终编号

- DCBM-135 和 DCBM-136 均为 provisional。
- 读取执行时最后一个实际 DCBM ID。
- 仅对确认非重复候选连续分配最终编号。
- 重复候选不占号，不产生编号空洞。
- 不得修改既有记录编号。

六、正式写入与派生文件

仅对通过去重的候选：

1. 更新 00_Master/Deep_CBM_Latest.xlsx；
2. 保留全部 sheet、字段、格式、公式、超链接、批注和人工内容；
3. 新建 master snapshot，不覆盖历史 snapshot；
4. 生成 increment Excel；
5. 生成 increment RIS；
6. 生成 increment BibTeX；
7. 生成 increment DOI list；
8. 生成 duplicate check；
9. 生成 update log；
10. 重新生成：
    - 00_Master/index/Deep_CBM_master_index.jsonl
    - 00_Master/index/Deep_CBM_master_index.csv
    - 06_Statistics/Master_Index_Report_YYYYMMDD.md
    - QC report
11. 更新 CHANGELOG.md。

七、QC要求

确认：

- 工作簿可打开；
- 第一张 sheet 仍为完整文献矩阵；
- 8 个活动 sheet 完整保留；
- ID 连续且唯一；
- DOI_normalized 重复数为 0；
- 英文题名_normalized 重复数为 0；
- 中文题名_normalized 重复数为 0；
- 主表、JSONL 和 CSV 数量一致；
- increment Excel、RIS、BibTeX 和 DOI list 数量一致；
- skipped duplicate 包含原因和 existing ID；
- Online First/未来卷期状态准确；
- Candidate B 作者全名核验状态被记录；
- CHANGELOG 与实际新增数量一致；
- 保护目录未修改。

八、严格禁止修改

- 08_User/
- 00_Master/source/
- 00_Master/workbook_archive/
- 历史 snapshots
- 历史 increment
- 用户阅读标记、批注、自定义字段和人工排序

九、最终汇报

输出：

- status
- master_count_before
- master_count_after
- last_id_before
- last_id_after
- candidate_count
- added_count
- duplicate_skipped_count
- final_assigned_ids
- duplicate_skipped_details
- official_metadata_verified
- author_metadata_limitations
- online_first_statuses
- DOI_duplicate_count
- english_title_duplicate_count
- chinese_title_duplicate_count
- index_regenerated
- qc_report_path
- update_log_path
- increment_directory
- changelog_updated
- protected_paths_modified
- errors
- warnings
```

---

# 9. Daily ingest manifest

```json
{
  "brief_date": "2026-07-24",
  "brief_type": "candidate_update",
  "repository_source_of_truth_checked": true,
  "master_status_at_check": {
    "record_count": 134,
    "last_id": "DCBM-134",
    "id_continuous": true,
    "doi_missing_count": 2,
    "doi_duplicate_count": 0,
    "english_title_duplicate_count": 0,
    "chinese_title_duplicate_count": 0,
    "last_formal_update": "2026-07-23"
  },
  "recommended_add_count": 2,
  "manual_review_count": 0,
  "provisional_ids": ["DCBM-135", "DCBM-136"],
  "codex_action": "preflight_then_apply_verified_nonduplicates_only",
  "direct_repository_edit_performed": false,
  "protected_directory_edit_performed": false
}
```

---

# 10. 最终状态

```text
daily_brief_status: 2_recommended_candidates
repository_source_of_truth_checked: yes
master_record_count_at_check: 134
last_master_id_at_check: DCBM-134
recommended_add_count: 2
manual_review_count: 0
master_workbook_change_needed: pending_codex_live_deduplication
direct_repository_edit_performed: no
protected_directory_edit_performed: no
```
