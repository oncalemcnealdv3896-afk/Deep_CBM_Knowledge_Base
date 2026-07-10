# Deep CBM Daily Brief - 2026-07-10

## 1. 今日结论

今日基于 GitHub 当前主索引重新核验，并检索官方期刊页面后，确认 **3 篇建议入库候选文献**。另有 2 条潜在线索因期刊页面访问不稳定、题录信息未完成二次核验，本次不列为正式候选。

当前主库状态：

- 主库记录数：121
- 当前最后编号：`DCBM-121`
- 文献 ID 连续：是
- DOI 缺失：1
- DOI 重复：0
- 英文题名重复：0
- 中文题名重复：0
- 主索引来源：
  - `00_Master/index/Deep_CBM_master_index.jsonl`
  - `00_Master/index/Deep_CBM_master_index.csv`
  - `06_Statistics/Master_Index_Report_20260709.md`
- 最近一次主库更新：
  - `2026-07-09 Workbook Auxiliary Sheet Sync Patch`
  - 未新增文献，仅同步辅助 sheet 和重新生成 master index

> **重要说明**
>
> 下列 `DCBM-122` 至 `DCBM-124` 均为建议编号，不是最终编号。Codex 必须重新读取执行时刻的主工作簿和 master index，跳过重复项，并在当前最后一个实际编号之后连续分配最终 DCBM ID。

---

## 2. 检索范围与日期

- 检索日期：2026-07-10
- 上次有效检查基准：2026-07-09 Daily Brief corrected update
- 重点检索方向：
  - deep coalbed methane
  - deep CBM
  - deep coal-rock gas
  - coal-rock gas
  - deep coal measures gas
  - 深部煤层气
  - 深层煤岩气
  - 煤岩气
  - 鄂尔多斯盆地煤岩气
- 优先来源：
  - 官方期刊页面
  - 出版商页面
  - DOI 页面
  - GitHub master index
- 本次主要核验期刊：
  - *Petroleum Exploration and Development*

---

## 3. 当前主库状态与去重基础

根据 `Deep_CBM_master_index.jsonl` 和 `Master_Index_Report_20260709.md`：

| 项目 | 当前状态 |
|---|---:|
| 主库总记录数 | 121 |
| 当前最后编号 | DCBM-121 |
| 文献 ID 连续性 | 连续 |
| DOI 重复数 | 0 |
| 英文题名重复数 | 0 |
| 中文题名重复数 | 0 |

本次对候选执行了以下初筛：

1. DOI 完全匹配检查；
2. 英文题名规范化匹配；
3. 中文题名规范化匹配；
4. 第一作者—年份—题名组合检查；
5. 与最近日报候选及 2026-07-09 新增记录复核。

以下 3 篇候选的 DOI 和英文题名均未在当前 121 条 master index 中命中。

---

## 4. 今日候选总览

| Provisional ID | 处理建议 | 英文题名 | DOI | 官方来源 | 当前查重结果 |
|---|---|---|---|---|---|
| DCBM-122 | 建议入库 | Generation stages and genetic types of coal-rock gas in China | 10.11698/PED.20260096 | Petroleum Exploration and Development | DOI、英文题名未命中 |
| DCBM-123 | 建议入库 | Formation mechanism of coal-rock gas accumulation transition zones | 10.11698/PED.20260226 | Petroleum Exploration and Development | DOI、英文题名未命中 |
| DCBM-124 | 建议入库 | Cementing and film-forming hydrophobic drilling fluid technology for long horizontal wells in deep coal-rock gas reservoirs | 10.11698/PED.20260208 | Petroleum Exploration and Development | DOI、英文题名未命中 |

---

## 5. 候选详述

### DCBM-122 provisional

#### 基本信息

- 英文题名：Generation stages and genetic types of coal-rock gas in China
- 建议中文题名：中国煤岩气生成阶段及气藏成因类型
- 作者：ZHANG Shuichang; ZHANG Bin; MA Xingzhi; TANG Yong; LIANG Zeliang; SUN Longde
- 年份：2026
- 期刊：Petroleum Exploration and Development
- 卷期：53(3)
- 页码：533-544
- DOI：10.11698/PED.20260096
- 官方页面：https://www.cpedm.com/EN/10.11698/PED.20260096
- 收稿日期：2026-02-14
- 网络优先日期：2026-05-19
- 正式出版日期：2026-06-17

#### 研究对象与研究目的

该文聚焦中国煤岩气的生成阶段和成因类型，属于煤层气—深部煤岩气概念体系和成藏分类研究。其核心价值在于尝试从煤岩热演化、气体赋存状态、储层特征和生产表现等维度，对不同深度和不同演化阶段的煤系气资源进行统一认识。

#### 数据与方法

官方英文页面当前能够稳定核验题名、作者、卷期、页码、DOI 和出版时间，但摘要正文未正常加载。因此本次不能可靠提取具体样品数量、实验流程和定量参数。根据题名和文章类型，可判断其主要采用综合地质分析和成因分类方法，但该判断仍需 Codex 或人工阅读全文确认。

#### 主要发现

当前只能确认文章建立或讨论了中国煤岩气生成阶段与成因类型框架。更具体的分类边界、赋存相态演化和判别指标必须以全文为准，不应仅依据题名扩展为正式结论。

#### 创新与局限

可能的创新在于将浅层煤层气、深部煤岩气及相关煤系气类型置于统一演化框架下讨论。当前局限是官方网页摘要未正常显示，无法从公开页面核验具体分类数量、阈值和定量结论。

#### 与 Deep CBM 研究的关联

该文对用户当前先导井研究的直接数据贡献有限，但对以下内容高度相关：

- 深部煤层气与煤岩气概念边界；
- 深度增加后吸附气、游离气赋存关系变化；
- 不同类型气藏生产机制差异；
- 论文引言、理论基础和讨论章节的术语统一。

#### 建议引用章节

- 引言与研究背景；
- 深部煤层气/煤岩气概念与成藏类型；
- 排采响应差异的地质机理讨论；
- 开发模式与生产机制讨论。

#### 阅读优先级

**A**

---

### DCBM-123 provisional

#### 基本信息

- 英文题名：Formation mechanism of coal-rock gas accumulation transition zones
- 建议中文题名：煤岩气聚集过渡带形成机制
- 作者：LI Guoxin; ZHAO Qun; ZHANG Junfeng; LIU Dan; SUN Jian; ZHOU Tianqi; XIAO Yuhang
- 年份：2026
- 期刊：Petroleum Exploration and Development
- 卷期：53(3)
- 页码：545-558
- DOI：10.11698/PED.20260226
- 官方页面：https://www.cpedm.com/EN/10.11698/PED.20260226
- 收稿日期：2026-04-19
- 修回日期：2026-06-10
- 正式出版日期：2026-06-17

#### 研究对象与研究目的

该文研究煤岩气聚集过渡带的形成机制，重点应涉及煤岩气在区域成藏体系中的空间过渡、气体富集差异和地质边界特征。

#### 数据与方法

官方页面能够稳定核验题名、作者、卷期、页码、DOI 和出版日期，但摘要内容未正常加载。当前无法确认研究区、样品量、测井资料、地球化学数据或数值模拟方法。Codex 入库时应从 PDF 或正式中文页面补齐这些字段。

#### 主要发现

根据题名可确认文章提出或解释了煤岩气聚集过渡带的形成机制，但具体机制组成、控制因素和区域适用性尚不能从当前公开页面可靠提取。

#### 创新与局限

潜在创新是将“聚集过渡带”作为煤岩气成藏和有利区评价的独立对象。局限是当前摘要不可用，不能据此写入定量阈值、甜点范围或主控因素排序。

#### 与 Deep CBM 研究的关联

该文可作为解释先导井之间响应差异的区域地质背景文献，尤其适用于：

- 区块内富集带与过渡带划分；
- 井间含气性和储层品质差异解释；
- 响应类型与区域成藏位置之间的联系；
- 有利区和开发单元划分的理论支持。

#### 建议引用章节

- 区域地质背景；
- 煤岩气富集规律；
- 井间生产响应差异讨论；
- 地质—工程一体化评价。

#### 阅读优先级

**A**

---

### DCBM-124 provisional

#### 基本信息

- 英文题名：Cementing and film-forming hydrophobic drilling fluid technology for long horizontal wells in deep coal-rock gas reservoirs
- 建议中文题名：深层煤岩气长水平井胶结成膜固壁疏水钻井液技术
- 作者：SUN Jinsheng; LIU Hongtao; HAN Jinliang; ZHAO Li; HAO Pengcheng; ZHANG Shangkun; PENG Chao; LONG Yifu; LIU Fan; HUANG Xianbin; JIN Jiafeng
- 年份：2026
- 期刊：Petroleum Exploration and Development
- 卷期：53(3)
- 页码：737-746
- DOI：10.11698/PED.20260208
- 官方页面：https://www.cpedm.com/EN/10.11698/PED.20260208
- 收稿日期：2026-04-09
- 修回日期：2026-05-28
- 网络优先日期：2026-06-03
- 正式出版日期：2026-06-17

#### 研究对象与研究目的

该文面向深层煤岩气长水平井钻井过程中的井壁稳定、孔裂隙封堵和流体侵入控制问题，属于钻完井工程技术研究。

#### 数据与方法

题名表明其技术路线包括胶结、成膜、固壁和疏水控制。官方页面未正常展示摘要，当前无法核验钻井液配方、实验温压条件、岩样类型、现场井数和性能提升幅度。

#### 主要发现

能够确认文章提出并验证了一套适用于深层煤岩气长水平井的胶结成膜固壁疏水钻井液技术。任何关于封堵率、膨胀抑制率、井径扩大率或现场提速幅度的数字均需阅读全文后再写入。

#### 创新与局限

潜在创新是将孔裂隙封堵、胶结成膜、井壁强化和疏水抑制组合到同一钻井液体系中。该文与排采动态并非直接同类研究，更多属于工程背景和井筒质量影响因素文献。

#### 与 Deep CBM 研究的关联

该文可用于解释钻完井质量对后续压裂、排液、井筒完整性和生产稳定性的潜在影响，但不宜直接用于排采动态分型或产能主控因素排序。

#### 建议引用章节

- 深部煤岩气工程技术背景；
- 水平井钻完井难点；
- 地质—工程影响因素讨论；
- 研究局限与工程资料缺失说明。

#### 阅读优先级

**B**

---

## 6. Matrix-ready rows

| 序号 | 文献ID | 第一作者 | 全部作者 | 年份 | 英文题名 | 中文题名 | 期刊/来源 | 卷 | 期 | 页码/文章号 | DOI | 官方网页 | 文献类型 | 研究区域/区块 | 研究对象 | 研究目的 | 主要方法 | 核心结论 | 创新点 | 局限性 | 与课题关联 | 建议引用章节 | 关键词/标签 | 精读优先级 | 核验状态 |
|---|---|---|---|---:|---|---|---|---:|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 待定 | DCBM-122 provisional | ZHANG Shuichang | ZHANG Shuichang; ZHANG Bin; MA Xingzhi; TANG Yong; LIANG Zeliang; SUN Longde | 2026 | Generation stages and genetic types of coal-rock gas in China | 中国煤岩气生成阶段及气藏成因类型 | Petroleum Exploration and Development | 53 | 3 | 533-544 | 10.11698/PED.20260096 | https://www.cpedm.com/EN/10.11698/PED.20260096 | 理论/成藏分类 | 中国 | 煤层气与煤岩气 | 建立生成阶段与成因类型认识 | 综合地质与成因分析，具体方法待全文核验 | 建立煤岩气生成阶段和成因类型框架，细节待全文核验 | 统一不同深度煤系气成因认识 | 摘要未正常加载，定量信息待补 | 强相关，适合概念边界和生产机理讨论 | 引言；理论基础；讨论 | 煤岩气；生成阶段；成因类型；赋存状态 | A | 题名、作者、卷期页码、DOI、出版日期已核验 |
| 待定 | DCBM-123 provisional | LI Guoxin | LI Guoxin; ZHAO Qun; ZHANG Junfeng; LIU Dan; SUN Jian; ZHOU Tianqi; XIAO Yuhang | 2026 | Formation mechanism of coal-rock gas accumulation transition zones | 煤岩气聚集过渡带形成机制 | Petroleum Exploration and Development | 53 | 3 | 545-558 | 10.11698/PED.20260226 | https://www.cpedm.com/EN/10.11698/PED.20260226 | 成藏机制 | 待全文核验 | 煤岩气聚集过渡带 | 解释聚集过渡带形成机制 | 地质综合分析，具体方法待全文核验 | 提出聚集过渡带形成机制，具体控制因素待全文核验 | 将过渡带作为独立成藏评价对象 | 摘要未正常加载，研究区和定量数据待补 | 强相关，可支持井间响应差异的区域地质解释 | 区域地质；富集规律；讨论 | 煤岩气；聚集过渡带；富集机制 | A | 题名、作者、卷期页码、DOI、出版日期已核验 |
| 待定 | DCBM-124 provisional | SUN Jinsheng | SUN Jinsheng; LIU Hongtao; HAN Jinliang; ZHAO Li; HAO Pengcheng; ZHANG Shangkun; PENG Chao; LONG Yifu; LIU Fan; HUANG Xianbin; JIN Jiafeng | 2026 | Cementing and film-forming hydrophobic drilling fluid technology for long horizontal wells in deep coal-rock gas reservoirs | 深层煤岩气长水平井胶结成膜固壁疏水钻井液技术 | Petroleum Exploration and Development | 53 | 3 | 737-746 | 10.11698/PED.20260208 | https://www.cpedm.com/EN/10.11698/PED.20260208 | 钻完井工程 | 待全文核验 | 深层煤岩气长水平井 | 提升井壁稳定和孔裂隙封堵能力 | 钻井液体系研发与现场验证，具体参数待全文核验 | 形成胶结成膜固壁疏水钻井液技术 | 多机制耦合的井壁稳定体系 | 与排采动态间接相关；定量结果待补 | 工程背景和井筒质量影响因素参考 | 工程背景；讨论 | 深层煤岩气；水平井；钻井液；井壁稳定 | B | 题名、作者、卷期页码、DOI、出版日期已核验 |

---

## 7. RIS block

```ris
TY  - JOUR
ID  - DCBM-122-provisional
AU  - Zhang, Shuichang
AU  - Zhang, Bin
AU  - Ma, Xingzhi
AU  - Tang, Yong
AU  - Liang, Zeliang
AU  - Sun, Longde
PY  - 2026
TI  - Generation stages and genetic types of coal-rock gas in China
T2  - Petroleum Exploration and Development
VL  - 53
IS  - 3
SP  - 533
EP  - 544
DO  - 10.11698/PED.20260096
UR  - https://www.cpedm.com/EN/10.11698/PED.20260096
N1  - Provisional ID; final ID must be reassigned after Codex rechecks the current master index.
ER  -

TY  - JOUR
ID  - DCBM-123-provisional
AU  - Li, Guoxin
AU  - Zhao, Qun
AU  - Zhang, Junfeng
AU  - Liu, Dan
AU  - Sun, Jian
AU  - Zhou, Tianqi
AU  - Xiao, Yuhang
PY  - 2026
TI  - Formation mechanism of coal-rock gas accumulation transition zones
T2  - Petroleum Exploration and Development
VL  - 53
IS  - 3
SP  - 545
EP  - 558
DO  - 10.11698/PED.20260226
UR  - https://www.cpedm.com/EN/10.11698/PED.20260226
N1  - Provisional ID; final ID must be reassigned after Codex rechecks the current master index.
ER  -

TY  - JOUR
ID  - DCBM-124-provisional
AU  - Sun, Jinsheng
AU  - Liu, Hongtao
AU  - Han, Jinliang
AU  - Zhao, Li
AU  - Hao, Pengcheng
AU  - Zhang, Shangkun
AU  - Peng, Chao
AU  - Long, Yifu
AU  - Liu, Fan
AU  - Huang, Xianbin
AU  - Jin, Jiafeng
PY  - 2026
TI  - Cementing and film-forming hydrophobic drilling fluid technology for long horizontal wells in deep coal-rock gas reservoirs
T2  - Petroleum Exploration and Development
VL  - 53
IS  - 3
SP  - 737
EP  - 746
DO  - 10.11698/PED.20260208
UR  - https://www.cpedm.com/EN/10.11698/PED.20260208
N1  - Provisional ID; final ID must be reassigned after Codex rechecks the current master index.
ER  -
```

---

## 8. BibTeX block

```bibtex
@article{DCBM122_provisional_Zhang_2026,
  title   = {Generation stages and genetic types of coal-rock gas in China},
  author  = {Zhang, Shuichang and Zhang, Bin and Ma, Xingzhi and Tang, Yong and Liang, Zeliang and Sun, Longde},
  journal = {Petroleum Exploration and Development},
  year    = {2026},
  volume  = {53},
  number  = {3},
  pages   = {533--544},
  doi     = {10.11698/PED.20260096},
  url     = {https://www.cpedm.com/EN/10.11698/PED.20260096},
  note    = {Provisional DCBM ID; recheck master index before import}
}

@article{DCBM123_provisional_Li_2026,
  title   = {Formation mechanism of coal-rock gas accumulation transition zones},
  author  = {Li, Guoxin and Zhao, Qun and Zhang, Junfeng and Liu, Dan and Sun, Jian and Zhou, Tianqi and Xiao, Yuhang},
  journal = {Petroleum Exploration and Development},
  year    = {2026},
  volume  = {53},
  number  = {3},
  pages   = {545--558},
  doi     = {10.11698/PED.20260226},
  url     = {https://www.cpedm.com/EN/10.11698/PED.20260226},
  note    = {Provisional DCBM ID; recheck master index before import}
}

@article{DCBM124_provisional_Sun_2026,
  title   = {Cementing and film-forming hydrophobic drilling fluid technology for long horizontal wells in deep coal-rock gas reservoirs},
  author  = {Sun, Jinsheng and Liu, Hongtao and Han, Jinliang and Zhao, Li and Hao, Pengcheng and Zhang, Shangkun and Peng, Chao and Long, Yifu and Liu, Fan and Huang, Xianbin and Jin, Jiafeng},
  journal = {Petroleum Exploration and Development},
  year    = {2026},
  volume  = {53},
  number  = {3},
  pages   = {737--746},
  doi     = {10.11698/PED.20260208},
  url     = {https://www.cpedm.com/EN/10.11698/PED.20260208},
  note    = {Provisional DCBM ID; recheck master index before import}
}
```

---

## 9. 暂不纳入正式候选的线索

本次还发现 2 条可能相关的 2026 年题录线索：

1. 鄂尔多斯盆地高阶煤岩气成藏地质特征及勘探潜力；
2. 鄂尔多斯盆地本溪组煤岩生烃—孔隙演化模拟。

由于本次访问相关期刊页面时出现超时或无法稳定获取题录，且检索结果未能完成作者、卷期、页码和 DOI 的独立二次核验，因此不列入本日报的正式 Matrix-ready 候选。后续应继续跟踪，而不是直接写入主表。

---

## 10. Codex 执行指令

请 Codex 严格按以下流程执行：

1. 执行 `git pull`，确保本地仓库是最新状态。
2. 重新读取：
   - `00_Master/Deep_CBM_Latest.xlsx`
   - `00_Master/index/Deep_CBM_master_index.jsonl`
   - `00_Master/index/Deep_CBM_master_index.csv`
   - 最新 `06_Statistics/Master_Index_Report_*.md`
   - `CHANGELOG.md`
   - 最近的 `09_Daily_Brief/`
3. 将本简报保存为：
   - `09_Daily_Brief/2026-07-10/Deep_CBM_daily_brief_20260710.md`
4. 对每个 provisional candidate 重新执行：
   - DOI_normalized 完全匹配；
   - 英文题名_normalized 匹配；
   - 中文题名_normalized 匹配；
   - 第一作者 + 年份 + 题名相似度检查。
5. **不得直接采用本简报中的 provisional ID。**
6. 如发现重复：
   - 跳过重复项；
   - 记录 skipped duplicate；
   - 记录重复原因；
   - 记录 existing DCBM ID；
   - 继续处理其他非重复候选。
7. 如 3 篇均不重复，则可从当前最后一个实际 ID 之后顺序编号；若执行时最后 ID 仍为 `DCBM-121`，建议最终编号为 `DCBM-122` 至 `DCBM-124`。
8. 从官方 PDF 或正式中文页面补齐：
   - 中文题名；
   - 研究区；
   - 数据与方法；
   - 样品量或井数；
   - 定量结果；
   - 创新点与局限；
   - 全部作者和基金信息。
9. 不得根据题名臆造摘要、阈值、样本量或定量结论。
10. 更新主工作簿后，同步维护所有辅助 sheet：
    - 完整文献矩阵；
    - 总览统计；
    - 网页索引；
    - 字段说明；
    - 精读摘要；
    - 更新日志；
    - 重复检查；
    - QC报告。
11. 重新生成：
    - `00_Master/index/Deep_CBM_master_index.jsonl`
    - `00_Master/index/Deep_CBM_master_index.csv`
    - `06_Statistics/Master_Index_Report_20260710.md`
    - `06_Statistics/QC_Report_20260710*.md`
    - `01_Increment/2026-07-10*/`
    - 增量 Excel、RIS、BibTeX、duplicate check 和 update log。
12. 更新 `CHANGELOG.md`。
13. **严禁修改：**
    - `08_User/`
    - `00_Master/source/`
    - `00_Master/workbook_archive/`
    - 既有 snapshot；
    - 既有历史 increment 文件。
14. 建议提交信息：
    - `update: add verified Deep CBM literature candidates 2026-07-10`

---

## 11. 来源清单

### GitHub 单一事实来源

- `00_Master/index/Deep_CBM_master_index.jsonl`
- `00_Master/index/Deep_CBM_master_index.csv`
- `06_Statistics/Master_Index_Report_20260709.md`
- `CHANGELOG.md`
- `09_Daily_Brief/2026-07-09/Deep_CBM_daily_brief_20260709.md`

### 官方期刊页面

- https://www.cpedm.com/EN/10.11698/PED.20260096
- https://www.cpedm.com/EN/10.11698/PED.20260226
- https://www.cpedm.com/EN/10.11698/PED.20260208

---

## 12. 最终处理建议

今日建议将 3 篇文献交给 Codex 做二次查重和全文补充，不应直接视为已入库记录。若执行时主库仍为 121 条且三篇均无重复，则主库更新后预计为 124 条，最后编号为 `DCBM-124`。
