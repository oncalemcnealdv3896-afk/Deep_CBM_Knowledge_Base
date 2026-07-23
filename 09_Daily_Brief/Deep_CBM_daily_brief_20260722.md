# Deep CBM Knowledge Base Daily Brief — 2026-07-22

> 建议保存路径：`09_Daily_Brief/2026-07-22/Deep_CBM_daily_brief_20260722.md`

## 1. 今日结论

本轮首先读取 GitHub 仓库 `oncalemcnealdv3896-afk/Deep_CBM_Knowledge_Base`，并将其作为唯一正式事实来源。当前主库仍为 **124 条记录，最后编号 DCBM-124**；文献 ID 连续，DOI、中英文题名均无重复。

随后对 2026-07-10 以来新近正式出版、Online First、近期完成 DOI 注册或近期可发现的深部煤层气、深部煤岩气和深部煤系气文献进行检索，并使用当前 master index 进行 DOI、题名和作者—年份去重。

### 今日筛选结果

- **建议 Codex 执行时再次查重后入库：10 篇**
- **仅建议人工复核、暂不自动入库：1 篇**
- **已确认与主库重复并排除：4 篇**
- **未直接修改 Excel、RIS、BibTeX 或 GitHub 仓库**

按日报生成时的主库状态，建议暂定编号如下：

| 暂定编号 | 状态 | 文献主题 |
|---|---|---|
| DCBM-125 | 建议入库 | 润湿性调控促进深部煤岩吸附态甲烷解吸 |
| DCBM-126 | 建议入库 | 深部煤储层高温高压吸附热力学与容量预测 |
| DCBM-127 | 建议入库 | 超高矿化度返排液复配滑溜水压裂液 |
| DCBM-128 | 建议入库 | 绥德区块深部煤储层孔隙结构多重分形 |
| DCBM-129 | 建议入库 | 鄂尔多斯深部煤大分子结构—纳米孔—吸附耦合 |
| DCBM-130 | 建议入库 | 深部中高阶煤吸附能量与甲烷赋存状态协同演化 |
| DCBM-131 | 建议入库 | 深部煤层气热采机理、技术与挑战综述 |
| DCBM-132 | 建议入库 | 基于元素判识的深部煤层气水平井储层评价 |
| DCBM-133 | 建议入库 | 考虑煤体结构差异的深层煤层气地应力预测 |
| DCBM-134 | 建议入库 | 华北深层煤层气保存条件与富集高产 |
| DCBM-135-MR | 仅人工复核 | 神府气田煤层气储层表征与三维地质建模 |

**所有编号均为 provisional。** Codex 必须在执行时重新读取最新主工作簿和 master index，跳过重复项，记录重复原因及 existing DCBM ID，并仅对非重复且通过正式核验的文献，从执行时最后一个实际 DCBM ID 后连续分配最终编号。`DCBM-135-MR` 不保留或占用最终编号。

---

## 2. GitHub 单一事实来源核验

### 已读取文件

- `00_Master/index/Deep_CBM_master_index.jsonl`
- `00_Master/index/Deep_CBM_master_index.csv`
- `06_Statistics/Master_Index_Report_20260710.md`
- `CHANGELOG.md`
- 仓库最新提交记录
- `09_Daily_Brief/` 预期最近日报路径

### 当前主库状态

| 项目 | 当前值 |
|---|---:|
| 主工作簿 | `00_Master/Deep_CBM_Latest.xlsx` |
| 主索引 JSONL | `00_Master/index/Deep_CBM_master_index.jsonl` |
| 主索引 CSV | `00_Master/index/Deep_CBM_master_index.csv` |
| 当前记录数 | 124 |
| 当前最后编号 | DCBM-124 |
| 文献 ID 连续 | 是 |
| DOI 缺失 | 1 |
| DOI 重复 | 0 |
| 英文题名重复 | 0 |
| 中文题名重复 | 0 |
| 最近正式更新 | 2026-07-10 |
| 最新正式提交 | `48f61d23f87d7e4f702dc2815f82c5591159c0dc` |

### 最近正式更新

2026-07-10 更新新增：

- DCBM-122：*Generation stages and genetic types of coal-rock gas in China*
- DCBM-123：*Formation mechanism of coal-rock gas accumulation transition zones*
- DCBM-124：*Cementing and film-forming hydrophobic drilling fluid technology for long horizontal wells in deep coal-rock gas reservoirs*

主库由 121 条增加至 124 条，并重新生成 master index、QC 报告和增量文件。保护目录 `08_User/`、`00_Master/source/` 和 `00_Master/workbook_archive/` 未被修改。

### 日报路径核查说明

`CHANGELOG.md` 引用了 `09_Daily_Brief/2026-07-10/Deep_CBM_daily_brief_20260710.md`，但本轮通过该预期路径直接读取时返回 404，仓库检索也未发现 2026-07-10 之后已提交的日报文件。因此：

- 本轮不把聊天历史中的日报或暂定编号视为正式入库状态；
- 增量起点仅依据 master index、Master Index Report、CHANGELOG 和最新提交；
- “上次正式检查”按 2026-07-10 处理。

---

## 3. 检索范围与方法

### 检索日期

- 2026-07-22

### 时间窗口

- 重点增量窗口：2026-07-10 至 2026-07-22
- 补充窗口：2026 年近期正式进入卷期、Online First、未来卷期已注册 DOI 或近期被主要数据库发现的相关论文

### 英文检索词

- `"deep coalbed methane" 2026`
- `"deep CBM" July 2026`
- `"deep coal-rock gas" 2026`
- `"deep coal measures gas" 2026`
- `"deep coal reservoir" methane adsorption`
- `"deep coal seam" permeability`
- `"deep coalbed methane" fracturing fluid`
- `"deep coalbed methane" in-situ stress`
- `"deep coalbed methane" preservation`
- `"deep coalbed methane" thermal recovery`
- `"deep coal" pore structure multifractal`

### 中文检索词

- 深部煤层气
- 深层煤层气
- 深部煤岩气
- 深部煤系气
- 深部煤储层
- 深部煤层气吸附
- 深部煤层气润湿性
- 深部煤层气压裂液
- 深层煤层气地应力
- 深层煤层气保存条件
- 深部煤层气热采
- 深部煤孔隙分形

### 优先来源

- ACS Publications
- Elsevier / ScienceDirect
- Springer Nature
- DOI 注册页面
- 《煤炭科学技术》
- 《石油科学通报》
- 其他正式期刊页及主要文献数据库

### 去重顺序

1. DOI_normalized 精确匹配；
2. 英文题名_normalized 精确匹配；
3. 中文题名_normalized 精确匹配；
4. 第一作者—年份—题名组合；
5. Online First、Early Access、预出版和正式卷期版本合并判断；
6. 同一研究的中英文版本、会议稿和期刊稿人工复核；
7. 对无 DOI 或元数据冲突的候选降低自动入库等级。

---

# 4. 建议正式候选

## DCBM-125 provisional

### 基本信息

- 英文题名：Mechanism of Wettability Alteration to Unlock Adsorbed-State Methane in Deep Coal Rock: Insight from Experiment and Molecular Simulation
- 建议中文题名：深部煤岩润湿性调控促进吸附态甲烷释放机理：实验与分子模拟认识
- 第一作者：Tao Zhang
- 作者：Tao Zhang; Jianchun Guo; Zhihong Zhao; Jie Zeng
- 年份：2026
- 期刊：Energy & Fuels
- 在线发表：2026-07-10
- DOI：`10.1021/acs.energyfuels.6c02337`
- 官方页面：<https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02337>
- 推荐状态：建议入库
- 阅读优先级：A

### 去重结果

- 当前 master index 未检出该 DOI；
- 未检出相同英文题名；
- 未检出相同中文题名；
- 当前判断为非重复候选。

### 研究对象与方法

研究针对深部煤岩中吸附态甲烷难以有效解吸的问题，采用表面活性剂型压裂液改变煤岩润湿性，并结合：

- 自发渗吸实验；
- 孔隙结构表征；
- 甲烷吸附—解吸实验；
- 分子动力学模拟；
- 煤—甲烷—水相互作用能与配位数分析。

### 主要发现

- 渗吸作用可使部分“墨水瓶状”孔隙向狭缝型孔隙转化；
- 0.3–1.5 nm 纳米孔数量增加约 59.6%；
- 2–10 nm 孔隙增加约 44.8%；
- 甲烷—煤配位数由约 16.2 降至 12.3；
- 水—煤配位数由接近 0 增至约 9.6；
- 水分子优先占据煤表面并形成稳定吸附水膜；
- 甲烷脱附表观能垒由约 1500 kJ/mol 降至约 800 kJ/mol。

### 创新与局限

**创新：**

- 将润湿性改变、孔隙结构演化和吸附态甲烷释放统一解释；
- 以分子尺度证据说明水膜竞争吸附对甲烷解吸的促进作用；
- 为深部煤岩气压裂液兼顾改造和解吸提供机制依据。

**局限：**

- 分子模型与实验煤样仍不能完全代表井尺度非均质性；
- 能垒数值依赖模型、力场和计算边界；
- 润湿性改善不等同于长期产能必然增加；
- 表面活性剂体系的地层适配性、返排和环境影响仍需现场验证。

### 与用户研究的相关性

**极高。**

可支撑用户论文中：

- 水锁和液相滞留；
- 润湿性对气水运移的影响；
- 吸附气解吸启动；
- 裂缝—基质传质；
- 压裂液体系作为早期动态差异的候选解释。

### 建议引用章节

- 引言：深部煤层吸附气释放难点；
- 讨论：水锁、润湿性和解吸启动；
- 讨论：裂缝—基质传质；
- 局限：实验和分子尺度不能直接外推到井级产能。

---

## DCBM-126 provisional

### 基本信息

- 英文题名：Adsorption Thermodynamic Property of Deep Coal Reservoirs and Adsorption Capacity Prediction under Different Temperature and Pressure Conditions
- 建议中文题名：深部煤储层吸附热力学性质及不同温压条件下吸附容量预测
- 第一作者：Xiangchun Chang
- 作者：Xiangchun Chang; Shangbin Wang; Junjian Zhang; Bingbing Shi; Veerle Vandeginste; Yu Liu; Pengfei Zhang
- 年份：2026
- 期刊：Energy & Fuels
- 在线发表：2026-07-10
- DOI：`10.1021/acs.energyfuels.6c02529`
- 官方页面：<https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02529>
- 推荐状态：建议入库
- 阅读优先级：A−

### 研究区、数据与方法

研究对象为鄂尔多斯盆地东缘本溪组深部煤储层，使用来自 3 口井的 17 件煤样，开展：

- 工业分析；
- CO₂ 吸附实验；
- 高温高压甲烷等温吸附实验；
- 等量吸附热计算；
- 半经验模型和回归预测；
- 灰分、固定碳、微孔体积与 Langmuir 参数相关分析。

### 主要发现

- 灰分与微孔体积和甲烷吸附能力总体负相关；
- 固定碳和微孔体积与 Langmuir 体积正相关；
- 温度升高使吸附容量下降；
- 压力升高使吸附容量增加；
- 在高压条件下，温度对吸附容量的抑制更明显；
- 所建模型可用于研究温压范围内的吸附容量预测。

### 创新与局限

**创新：**

- 基于多井、多样品高温高压实验建立深部条件吸附模型；
- 将煤质、微孔和吸附热力学参数联系；
- 可为不同埋深温压条件下吸附气评估提供方法基础。

**局限：**

- 模型适用范围受实验温度、压力和煤阶限制；
- 外推至其他盆地前需要独立验证；
- 吸附容量不等同于可采气量；
- 未直接解决现场气水两相和应力敏感问题。

### 与用户研究的相关性

**高。**

可支撑：

- 深部温压条件对吸附气的影响；
- 游离气—吸附气贡献差异；
- 深度和煤质差异的替代解释；
- 用户项目不能仅凭早期产量反演储层吸附容量。

### 建议引用章节

- 引言：深部温压条件和吸附特征；
- 讨论：吸附气和游离气阶段性贡献；
- 局限：实验吸附容量与井级动态的差异。

---

## DCBM-127 provisional

### 基本信息

- 英文题名：Bioinspired by Mussels: Construction of an Ultrasalt-Tolerant, Tunable-Viscosity Slickwater Fracturing Fluid for the Reuse of Deep Coalbed Methane Flowback Fluids
- 建议中文题名：贻贝仿生超耐盐可调黏滑溜水压裂液及其在深部煤层气返排液回用中的应用
- 第一作者：Pingli Liu
- 作者：Pingli Liu; Chengwei Zuo; Juan Du; Jiahao Li; Xin Zhang; Renyin Zhao
- 年份：2026
- 期刊：Langmuir
- 在线发表：2026-07-14
- DOI：`10.1021/acs.langmuir.6c01692`
- 官方页面：<https://pubs.acs.org/doi/10.1021/acs.langmuir.6c01692>
- 推荐状态：建议入库
- 阅读优先级：A−

### 数据与方法

研究构建具有疏水缔合和反聚电解质效应的仿生耐盐聚合物减阻剂 ASD，并开展：

- 超高矿化度返排液配伍；
- 流变性与可调黏度测试；
- 减阻率测试；
- 支撑剂携砂性能；
- 破胶和残渣评价；
- 聚合物水化尺寸表征；
- 分子动力学模拟。

### 主要发现

- 在总溶解固体超过 120,000 mg/L 的返排液中，体系黏度仍可维持约 75 mPa·s；
- 最大减阻率约 79.58%；
- 具备较强支撑剂输送能力；
- 在 60 ℃ 条件下约 3 h 内可破胶；
- 破胶残渣约 310 mg/L；
- ASD 水化尺度约 500–2000 nm，明显高于普通 HPAM 的 10–35 nm；
- 分子模拟解释了其高盐环境下的结构适应性。

### 创新与局限

**创新：**

- 将返排液回用、耐盐、减阻和携砂整合；
- 利用仿生结构和反聚电解质效应提高超高盐适应性；
- 对深部煤层气压裂液循环利用具有工程价值。

**局限：**

- 实验条件与现场多轮剪切、复杂离子和煤粉环境存在差异；
- 残渣和地层伤害仍需长期评价；
- 压裂液性能不能直接证明产气提升；
- 与用户项目的关系应作为工程候选机制而非已证实原因。

### 与用户研究的相关性

**高。**

可支撑：

- 返排率低和液相滞留；
- 压裂液性质对早期排采的影响；
- 水锁和煤粉运移；
- 压裂改造差异作为响应曲线异质性的替代解释。

### 建议引用章节

- 讨论：返排、水锁和液相滞留；
- 讨论：压裂液和支撑剂运移；
- 局限：工程材料性能与生产动态之间不能直接建立因果。

---

## DCBM-128 provisional

### 基本信息

- 英文题名：Multifractal Characteristics of Pore Structure in Deep Coal Reservoirs of the Suide Block, Ordos Basin
- 建议中文题名：鄂尔多斯盆地绥德区块深部煤储层孔隙结构多重分形特征
- 第一作者：Yunhe Shi
- 作者：Yunhe Shi; Chang Xu; Kangle Wang; Hui Zhang; Chen Liang; Huaichang Wang; Jingjing Cao; Xueyuan Jing; Yi Du
- 年份：2026
- 期刊：ACS Omega
- 在线发表：2026-07-01
- DOI：`10.1021/acsomega.6c04169`
- 官方页面：<https://pubs.acs.org/doi/10.1021/acsomega.6c04169>
- 推荐状态：建议入库
- 阅读优先级：A−

### 研究区与方法

研究区为鄂尔多斯盆地绥德区块本溪组 8 号煤，样品来自 4 口井，埋深约 2250–2550 m，共 9 件煤样。方法包括：

- 场发射扫描电镜；
- 低温 CO₂ 吸附；
- 低温 N₂ 吸附；
- 高压压汞；
- 多重分形广义维数谱；
- 奇异谱；
- 灰分、固定碳和成熟度相关分析。

### 主要发现

- 研究煤样为高阶无烟煤，平均最大镜质体反射率约 2.57%；
- 孔隙以有机质孔为主；
- 摘要报告微孔平均占孔隙系统约 86.26%；
- 结论部分给出约 87.78%，两处存在轻微表述差异，入库摘要应保留来源差异；
- 微孔、中孔和大孔均呈多重分形；
- 大孔非均质性最高、连通性最差；
- 灰分降低孔容，并显著削弱中孔和大孔连通性。

### 创新与局限

**创新：**

- 将多尺度孔隙实验与多重分形联合；
- 分别评价微孔、中孔和大孔的异质性和连通性；
- 为吸附、扩散和渗流的尺度差异提供定量基础。

**局限：**

- 样本量较小；
- 分形参数与井尺度产能之间缺乏直接验证；
- 摘要和结论的微孔比例存在轻微差异，Codex 不应擅自统一；
- 孔隙结构证据不能直接证明用户项目的响应机制。

### 与用户研究的相关性

**高。**

可支撑：

- 微孔主导吸附储集；
- 中大孔和裂缝控制流动；
- 裂缝—基质传质；
- 储层异质性和小样本解释边界。

### 建议引用章节

- 引言：深部煤储层多尺度孔隙；
- 讨论：吸附—扩散—渗流；
- 局限：实验尺度与井尺度差异。

---

## DCBM-129 provisional

### 基本信息

- 英文题名：Linking macromolecular structure, nanopore evolution and methane adsorption in deep Ordos Basin coal: A mechanistic insight
- 建议中文题名：鄂尔多斯盆地深部煤大分子结构、纳米孔演化与甲烷吸附耦合机制
- 第一作者：Yan Shao
- 作者：Yan Shao; Yu Liu; Shaoqing Wang; Zilong Fu; Xiaoling Wang; Wanglin Xu
- 年份：2026
- 期刊：Journal of Molecular Structure
- 卷：1364
- 文章号：145895
- 日期：2026-07-05
- DOI：`10.1016/j.molstruc.2026.145895`
- 官方页面：<https://doi.org/10.1016/j.molstruc.2026.145895>
- 推荐状态：建议入库
- 阅读优先级：A−

### 数据与方法

研究使用鄂尔多斯盆地本溪组不同成熟度煤样，Ro 约 0.98%–1.79%，开展：

- 固体 13C NMR；
- FTIR；
- 高压压汞；
- N₂ 和 CO₂ 吸附；
- 甲烷等温吸附；
- 大分子结构、纳米孔和吸附参数联合分析。

### 主要发现

- 小于 1 nm 的微孔贡献超过 50% 孔体积和 90% 比表面积；
- 随成熟度升高，芳香度和缩合程度增加；
- 脂肪链和含氧官能团减少；
- 约 Ro 1.20% 附近出现两阶段结构—孔隙演化转折；
- 大分子结构演化通过控制超微孔和表面化学影响甲烷吸附。

### 创新与局限

**创新：**

- 把煤大分子结构、纳米孔演化和甲烷吸附放入统一机制框架；
- 识别成熟度相关的阶段性转折；
- 对深部不同煤阶储层的吸附差异提供微观解释。

**局限：**

- 样品代表性和转折阈值具有区域依赖；
- 吸附实验不能直接反映气水两相和应力路径；
- Ro 阈值不能直接用于用户井分类。

### 与用户研究的相关性

**高。**

适合支撑：

- 煤阶差异；
- 吸附气潜力；
- 基质孔隙和扩散；
- 不同井早期动态的储层替代解释。

### 建议引用章节

- 引言：煤阶和纳米孔背景；
- 讨论：基质扩散和吸附；
- 局限：微观结构不能直接推出井级响应。

---

## DCBM-130 provisional

### 基本信息

- 英文题名：Co-evolution of adsorption energetics and methane occurrence state in deep mid-to high-rank coal seams: implications for development
- 建议中文题名：深部中高阶煤层吸附能量与甲烷赋存状态协同演化及其开发意义
- 第一作者：Shuai Xu
- 作者：Shuai Xu; Caifang Wu; Lei Yang; Fangfang Wang; Zhihua Yan; Yi Cheng; Ze Zhou
- 年份：2026
- 期刊：Physics and Chemistry of the Earth
- 卷：144，Part 2
- 文章号：104541
- 正式期次日期：2026-10
- DOI：`10.1016/j.pce.2026.104541`
- 官方页面：<https://doi.org/10.1016/j.pce.2026.104541>
- 推荐状态：建议入库，标注未来卷期/已在线
- 阅读优先级：A−

### 研究区与方法

研究区为榆社—武乡区块，围绕深部中高阶煤超临界甲烷吸附和赋存状态开展：

- 高温高压吸附；
- 吸附能量计算；
- Amankwah 模型指数 k 三步优化；
- 吸附气和总含气量随深度的转折分析；
- 中阶煤与高阶煤的热力学和动力学约束对比。

### 主要发现

- 吸附气转折深度附近煤—甲烷结合最强；
- 中阶煤开发更多受热力学吸附屏障约束；
- 高阶煤更多受扩散和动力学屏障制约；
- 有利开发区可能位于吸附气转折深度与总含气量转折深度之间；
- 吸附能量和赋存相态应联合用于深部煤层气甜点评价。

### 创新与局限

**创新：**

- 把吸附能量和甲烷相态随深度的变化联合起来；
- 区分中阶煤和高阶煤的开发限制；
- 为深部甜点深度区间提供热力学解释。

**局限：**

- 研究区和煤阶适用性明显；
- “有利深度区间”不能直接迁移到其他盆地；
- 未来卷期信息可能继续更新；
- 不应据此对用户样本做正式甜点或产能排序。

### 与用户研究的相关性

**高。**

可支撑：

- 游离气与吸附气转换；
- 深度和煤阶差异；
- 解吸启动和扩散限制；
- 早期动态与储层相态之间的保守讨论。

### 建议引用章节

- 引言：深部赋存相态；
- 讨论：吸附能量、解吸和扩散；
- 局限：区域深度阈值不可外推。

---

## DCBM-131 provisional

### 基本信息

- 英文题名：Thermal recovery technology of deep coalbed methane: mechanisms, technologies, and development challenges
- 建议中文题名：深部煤层气热采技术：机理、技术体系与开发挑战
- 第一作者：Tengze Ge
- 作者：Tengze Ge; Xianyue Xiong; Shuguang Li; Xiaohu Xu; Ersi Gao; Chengwang Wang; Chuangye Wang; Shuai-Shuai Liu; Kai Wei
- 年份：2026
- 期刊：Fuel
- 卷：424
- 文章号：139357
- 正式期次日期：2026-11-15
- DOI：`10.1016/j.fuel.2026.139357`
- 官方页面：<https://doi.org/10.1016/j.fuel.2026.139357>
- 推荐状态：建议入库，标注未来卷期/已在线
- 阅读优先级：B+

### 内容与方法

该文为深部煤层气热采综述，系统总结：

- 升温削弱甲烷吸附；
- 热—流—固耦合；
- 注热、热流体和电/微波等潜在技术；
- CO₂ 辅助热采；
- 热作用对裂隙、渗透率和解吸的影响；
- 能耗、传热效率和工程放大问题。

### 主要认识

- 升温可降低吸附能力并促进甲烷解吸；
- 热作用可能改善基质向裂缝的传质；
- 多物理场耦合决定现场效果；
- 深部地层中的热损失、能耗和材料耐久性是关键限制；
- CO₂ 辅助热采具有增强采收和封存协同潜力；
- 当前主要瓶颈仍是现场尺度经济性和长期可靠性。

### 创新与局限

**价值：**

- 综合深部煤层气热采理论、实验和工程方向；
- 对温度驱动解吸和传质提供系统文献入口；
- 可作为未来研究展望文献。

**局限：**

- 综述不能替代项目直接证据；
- 许多技术仍停留在实验或模拟阶段；
- 不适合用于用户项目当前排采制度结论。

### 与用户研究的相关性

**中高。**

可用于：

- 深部温度对吸附和解吸的影响；
- 裂缝—基质传质；
- 后续提高采收率研究展望；
- 当前研究不能推断热采效果的边界声明。

### 建议引用章节

- 讨论：温度和解吸；
- 局限与展望：深部热采和 CO₂ 协同；
- 结论：未来独立验证需求。

---

## DCBM-132 provisional

### 基本信息

- 中文题名：基于元素判识的深部煤层气水平井储层评价
- 英文题名：Reservoir evaluation for deep coalbed methane horizontal wells based on elemental identification
- 第一作者：YUAN Beijie / 袁蓓洁
- 作者：YUAN Beijie; ZHANG Shicheng; XIAO Cong; HE Jiayuan
- 年份：2026
- 期刊：Petroleum Science Bulletin / 石油科学通报
- 卷期：11(3)
- 页码：819–835
- Online：2026-06-15
- Published：2026-06-30
- DOI：`10.3969/j.issn.2096-1693.2026.01.015`
- 官方页面：<https://sykxtb.cup.edu.cn/EN/10.3969/j.issn.2096-1693.2026.01.015>
- 推荐状态：建议入库
- 阅读优先级：A−

### 研究区、数据与方法

研究区为鄂尔多斯盆地东缘大牛地气田 8 号煤层。方法包括：

- 扫描电镜与能谱；
- 宏观煤岩类型识别；
- Pearson 相关和互信息筛选；
- 10 项元素特征；
- Logistic Regression、KNN、SVM、Decision Tree、Random Forest、Gradient Boosting、XGBoost、LightGBM；
- 混淆矩阵和 F1 Score；
- 3 口水平井实钻轨迹验证。

### 主要发现

- 光亮煤的 Al、Si、Ti、V、Zr 总体较低；
- P、S、Ca 相对较高；
- SVM 综合性能最好；
- 最优 F1 Score 为 85.9%；
- 3 口水平井预测准确率超过 80%；
- 可为压裂甜点选段和簇间布置提供参考。

### 创新与局限

**创新：**

- 使用元素判识和机器学习预测水平井煤岩类型；
- 以实际井轨迹进行验证；
- 为随钻储层评价提供新入口。

**局限：**

- 模型区块依赖明显；
- 跨仪器和跨区块迁移性未知；
- 分类准确率不能等同于产气效果；
- 不得据此建立用户项目主控因素排序。

### 与用户研究的相关性

**高。**

可支撑：

- 多源资料整合；
- 特征可用性；
- 储层异质性；
- 机器学习在深部煤层气中的谨慎定位。

### 建议引用章节

- 引言：智能评价；
- 方法讨论：特征筛选和模型验证；
- 局限：小样本与外部可迁移性。

---

## DCBM-133 provisional

### 基本信息

- 中文题名：考虑煤体结构差异的深层煤层气地应力场预测方法
- 英文题名：Prediction of in-situ stress field of deep coalbed methane considering coalbed structure differences
- 第一作者：CHEN Zhengrong / 陈正荣
- 作者：CHEN Zhengrong; LIU Wei; SHI Xian; XIE Xin; GE Xiaoxin; LI Guowu
- 年份：2026
- 期刊：Coal Science and Technology / 煤炭科学技术
- 卷期：54(2)
- DOI：`10.12438/cst.2025-0365`
- 官方页面：<https://www.mtkxjs.com.cn/article/doi/10.12438/cst.2025-0365>
- 页码状态：官方 HTML 显示 360–369，PDF/检索片段出现 375–384，存在元数据冲突
- 推荐状态：建议入库，但 Codex 必须先核实最终页码
- 阅读优先级：A

### 研究区与方法

研究区为鄂尔多斯盆地东缘深层煤层气区，主要方法包括：

- 煤岩动态和静态力学试验；
- 声发射原位应力测试；
- P、S 波转换；
- 声波、密度和井径建立煤体结构指数；
- 上覆载荷、构造应变和孔隙压力耦合单井应力模型；
- 小型压裂闭合压力验证；
- 有限元三维应力反演。

### 主要发现

- 最大和最小构造应变约为 0.29 和 0.11；
- 最大水平应力平均相对误差约 9.19%；
- 最小水平应力平均相对误差约 9.54%；
- 区域总体为正断层应力机制；
- 较小水平应力差有利于复杂裂缝网络形成；
- 顶底板—煤层应力差会限制裂缝垂向扩展；
- 煤体结构差异是深部应力预测不可忽略的因素。

### 创新与局限

**创新：**

- 显式考虑煤体结构差异；
- 将单井测井、力学实验、小型压裂和有限元反演结合；
- 对压裂裂缝形态提供应力依据。

**局限：**

- 页码元数据存在冲突，入库前必须核验；
- 应力模型具有区块和参数依赖；
- 应力结果不能直接证明用户井早期曲线成因；
- 不得将其用于正式主控因素排序。

### 与用户研究的相关性

**极高。**

可支撑：

- 深部高应力和应力敏感；
- 裂缝扩展和压降传播；
- 压裂改造差异；
- 井间早期响应的替代工程解释。

### 建议引用章节

- 引言：深部地应力背景；
- 讨论：应力敏感和裂缝扩展；
- 局限：缺少项目井直接应力资料。

---

## DCBM-134 provisional

### 基本信息

- 中文题名：华北地区深层煤层气保存条件对富集高产的影响研究
- 英文题名：Controls of deep coalbed methane preservation conditions on enrichment and high productivity in North China
- 第一作者：GUO Xusheng / 郭旭升
- 作者：GUO Xusheng; LIU Zengqin; ZHAO Peirong; SHEN Baojian; ZHAO Shihu; YE Jincheng; ZHANG Jiaqi; WAN Junyu; CHEN Xinjun; QIU Feng; SHAO Yanwen; WANG Tianyun; DING Anxu; MA Chao
- 年份：2026
- 期刊：Petroleum Science Bulletin / 石油科学通报
- 卷期：11(1)
- 页码：2–13
- DOI：`10.3969/j.issn.2096-1693.2026.01.001`
- 官方页面：<https://sykxtb.cup.edu.cn/EN/10.3969/j.issn.2096-1693.2026.01.001>
- 推荐状态：建议入库
- 阅读优先级：A−

### 研究区与方法

研究对象为华北地区埋深大于约 1500 m 的深层煤层气。论文综合：

- 地质资料；
- 地球化学资料；
- 地球物理资料；
- 煤质和岩性组合；
- 典型井与区块对比；
- 吸附自封闭、物性封闭和构造保存分析。

### 主要认识

- 深层煤层气富集高产不仅受含气性控制，也显著受保存条件控制；
- 吸附自封闭、低渗物性封闭和构造保存共同作用；
- 盖层、断裂活动和构造演化决定气体散失风险；
- 良好保存区更可能形成高含气和高产组合；
- 论文估计华北深层煤层气资源规模超过 30 万亿 m³，但该数字应按原文口径使用，不与用户项目资源量直接关联。

### 创新与局限

**价值：**

- 将保存条件提升为深层煤层气富集高产的重要约束；
- 综合多种证据类型；
- 适合支撑成藏和区域差异讨论。

**局限：**

- 区域尺度结论不能直接解释单井早期动态；
- 资源量估计受评价口径影响；
- 保存条件需由项目地质和压力资料独立验证。

### 与用户研究的相关性

**中高。**

可用于：

- 研究背景和深部成藏；
- 区域差异和替代解释；
- 强调项目动态数据不能单独证明富集保存机制。

### 建议引用章节

- 引言：华北深层煤层气资源与保存；
- 讨论：地质背景和区域差异；
- 局限：单井动态无法证明区域保存条件。

---

# 5. 仅人工复核候选

## DCBM-135-MR — manual review only

### 基本信息

- 英文题名：Coalbed Methane Reservoir Characterization and Geological Modeling: A Case Study of Block A in the Shenfu Gas Field, Eastern Margin of the Ordos Basin
- 建议中文题名：鄂尔多斯盆地东缘神府气田 A 区块煤层气储层表征与地质建模
- 第一作者：Di Yang
- 作者：Di Yang; Yongjing Tian; Maojun Fang; Yuhu Bai; Yu Qi; Fen Liu; Ruyong Feng; Hao Lu
- 年份：2026
- 期刊：ACS Omega
- 在线发表：2026-07-17
- DOI：`10.1021/acsomega.6c01024`
- 官方页面：<https://pubs.acs.org/doi/10.1021/acsomega.6c01024>
- 状态：manual review only
- 阅读优先级：B+

### 研究内容

研究神府气田 A 区块本溪组 8+9 号煤层，采用：

- 岩心观察和实验；
- 测井标定；
- 煤岩类型识别；
- 三维岩性建模；
- 三维含气量建模；
- 生产资料验证。

论文认为光亮煤和半亮煤为较有利储层类型，优势区在平面上偏中部、纵向上偏煤层中上部。

### 暂不自动入库原因

- 题名未明确使用 deep/deep CBM；
- 虽研究位于深部煤层气重要区带，但公开信息中埋深与“深部”判据需进一步核验；
- 应与主库纳入边界进行人工相关性判断；
- 在确定目标层埋深、研究定位和与深部煤层气的直接关系前，不占用最终编号。

### Codex 转正条件

只有满足以下条件才可正式入库：

1. 官方全文明确研究对象符合当前知识库深部煤层气纳入标准；
2. DOI、题名、作者和年份与 master index 不重复；
3. 记录研究层位、埋深及深部相关性依据；
4. 人工复核结论为 `include`。

---

# 6. 已确认重复并排除

| DOI | 题名 | 已有 ID | 排除理由 |
|---|---|---|---|
| `10.1016/j.engeos.2026.100609` | Dynamic monitoring and effectiveness evaluation of mid-deep coalbed methane hydraulic fracturing via the wide-field electromagnetic method | DCBM-115 | DOI和英文题名完全匹配 |
| `10.13225/j.cnki.jccs.QH25.0479` | Productivity prediction and production performances of deep coalbed methane horizontal wells throughout full life cycle | DCBM-121 | DOI和英文题名完全匹配 |
| `10.1038/s41598-026-54924-z` | Evaluating deep coal rock gas fracturing sweet spot intervals using PSO-ELM algorithm and petrophysical logging data | DCBM-119 | DOI和题名完全匹配 |
| `10.3389/feart.2026.1772109` | Evaluation of development effectiveness of deep coalbed methane based on flowback characteristics | DCBM-028 | DOI已在历史日报处理中确认为重复 |

上述文献不得再次分配 provisional ID 或写入主工作簿。

---

# 7. Matrix-ready rows

| provisional_id | recommendation | DOI | 英文题名 | 中文题名 | 第一作者 | 年份 | 期刊/来源 | 卷期/文章号 | 官方网页 | 核验状态 | 优先级 |
|---|---|---|---|---|---|---:|---|---|---|---|---|
| DCBM-125 | add_after_live_dedup | 10.1021/acs.energyfuels.6c02337 | Mechanism of Wettability Alteration to Unlock Adsorbed-State Methane in Deep Coal Rock: Insight from Experiment and Molecular Simulation | 深部煤岩润湿性调控促进吸附态甲烷释放机理 | Tao Zhang | 2026 | Energy & Fuels | Online 2026-07-10 | https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02337 | 官方 ACS 页面核验题名、作者、DOI、日期和摘要 | A |
| DCBM-126 | add_after_live_dedup | 10.1021/acs.energyfuels.6c02529 | Adsorption Thermodynamic Property of Deep Coal Reservoirs and Adsorption Capacity Prediction under Different Temperature and Pressure Conditions | 深部煤储层吸附热力学性质及不同温压条件下吸附容量预测 | Xiangchun Chang | 2026 | Energy & Fuels | Online 2026-07-10 | https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02529 | 官方 ACS 页面核验 | A− |
| DCBM-127 | add_after_live_dedup | 10.1021/acs.langmuir.6c01692 | Bioinspired by Mussels: Construction of an Ultrasalt-Tolerant, Tunable-Viscosity Slickwater Fracturing Fluid for the Reuse of Deep Coalbed Methane Flowback Fluids | 贻贝仿生超耐盐可调黏滑溜水压裂液及返排液回用 | Pingli Liu | 2026 | Langmuir | Online 2026-07-14 | https://pubs.acs.org/doi/10.1021/acs.langmuir.6c01692 | 官方 ACS 页面核验 | A− |
| DCBM-128 | add_after_live_dedup | 10.1021/acsomega.6c04169 | Multifractal Characteristics of Pore Structure in Deep Coal Reservoirs of the Suide Block, Ordos Basin | 绥德区块深部煤储层孔隙结构多重分形特征 | Yunhe Shi | 2026 | ACS Omega | Online 2026-07-01 | https://pubs.acs.org/doi/10.1021/acsomega.6c04169 | 官方 ACS 页面核验；微孔比例存在源内轻微差异 | A− |
| DCBM-129 | add_after_live_dedup | 10.1016/j.molstruc.2026.145895 | Linking macromolecular structure, nanopore evolution and methane adsorption in deep Ordos Basin coal: A mechanistic insight | 深部煤大分子结构、纳米孔演化与甲烷吸附耦合机制 | Yan Shao | 2026 | Journal of Molecular Structure | 1364:145895 | https://doi.org/10.1016/j.molstruc.2026.145895 | DOI及出版商题录核验 | A− |
| DCBM-130 | add_after_live_dedup | 10.1016/j.pce.2026.104541 | Co-evolution of adsorption energetics and methane occurrence state in deep mid-to high-rank coal seams: implications for development | 深部中高阶煤吸附能量与甲烷赋存状态协同演化 | Shuai Xu | 2026 | Physics and Chemistry of the Earth | 144 Part 2:104541 | https://doi.org/10.1016/j.pce.2026.104541 | DOI及出版商题录核验；未来卷期 | A− |
| DCBM-131 | add_after_live_dedup | 10.1016/j.fuel.2026.139357 | Thermal recovery technology of deep coalbed methane: mechanisms, technologies, and development challenges | 深部煤层气热采技术：机理、技术与挑战 | Tengze Ge | 2026 | Fuel | 424:139357 | https://doi.org/10.1016/j.fuel.2026.139357 | DOI及出版商题录核验；未来卷期 | B+ |
| DCBM-132 | add_after_live_dedup | 10.3969/j.issn.2096-1693.2026.01.015 | Reservoir evaluation for deep coalbed methane horizontal wells based on elemental identification | 基于元素判识的深部煤层气水平井储层评价 | YUAN Beijie | 2026 | Petroleum Science Bulletin | 11(3):819–835 | https://sykxtb.cup.edu.cn/EN/10.3969/j.issn.2096-1693.2026.01.015 | 官方期刊页核验 | A− |
| DCBM-133 | add_after_metadata_resolution | 10.12438/cst.2025-0365 | Prediction of in-situ stress field of deep coalbed methane considering coalbed structure differences | 考虑煤体结构差异的深层煤层气地应力场预测方法 | CHEN Zhengrong | 2026 | Coal Science and Technology | 54(2)，页码待解决 | https://www.mtkxjs.com.cn/article/doi/10.12438/cst.2025-0365 | 官方页与PDF片段页码冲突，必须先核验 | A |
| DCBM-134 | add_after_live_dedup | 10.3969/j.issn.2096-1693.2026.01.001 | Controls of deep coalbed methane preservation conditions on enrichment and high productivity in North China | 华北地区深层煤层气保存条件对富集高产的影响研究 | GUO Xusheng | 2026 | Petroleum Science Bulletin | 11(1):2–13 | https://sykxtb.cup.edu.cn/EN/10.3969/j.issn.2096-1693.2026.01.001 | 官方期刊页核验 | A− |
| DCBM-135-MR | manual_review_only | 10.1021/acsomega.6c01024 | Coalbed Methane Reservoir Characterization and Geological Modeling: A Case Study of Block A in the Shenfu Gas Field, Eastern Margin of the Ordos Basin | 神府气田A区块煤层气储层表征与地质建模 | Di Yang | 2026 | ACS Omega | Online 2026-07-17 | https://pubs.acs.org/doi/10.1021/acsomega.6c01024 | 题录已核验，深部相关性需人工确认 | B+ |

---

# 8. RIS block

```ris
TY  - JOUR
ID  - DCBM-125-PROVISIONAL
AU  - Zhang, Tao
AU  - Guo, Jianchun
AU  - Zhao, Zhihong
AU  - Zeng, Jie
PY  - 2026
TI  - Mechanism of Wettability Alteration to Unlock Adsorbed-State Methane in Deep Coal Rock: Insight from Experiment and Molecular Simulation
T2  - Energy & Fuels
DO  - 10.1021/acs.energyfuels.6c02337
UR  - https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02337
N1  - Published online 2026-07-10. Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-126-PROVISIONAL
AU  - Chang, Xiangchun
AU  - Wang, Shangbin
AU  - Zhang, Junjian
AU  - Shi, Bingbing
AU  - Vandeginste, Veerle
AU  - Liu, Yu
AU  - Zhang, Pengfei
PY  - 2026
TI  - Adsorption Thermodynamic Property of Deep Coal Reservoirs and Adsorption Capacity Prediction under Different Temperature and Pressure Conditions
T2  - Energy & Fuels
DO  - 10.1021/acs.energyfuels.6c02529
UR  - https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02529
N1  - Published online 2026-07-10. Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-127-PROVISIONAL
AU  - Liu, Pingli
AU  - Zuo, Chengwei
AU  - Du, Juan
AU  - Li, Jiahao
AU  - Zhang, Xin
AU  - Zhao, Renyin
PY  - 2026
TI  - Bioinspired by Mussels: Construction of an Ultrasalt-Tolerant, Tunable-Viscosity Slickwater Fracturing Fluid for the Reuse of Deep Coalbed Methane Flowback Fluids
T2  - Langmuir
DO  - 10.1021/acs.langmuir.6c01692
UR  - https://pubs.acs.org/doi/10.1021/acs.langmuir.6c01692
N1  - Published online 2026-07-14. Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-128-PROVISIONAL
AU  - Shi, Yunhe
AU  - Xu, Chang
AU  - Wang, Kangle
AU  - Zhang, Hui
AU  - Liang, Chen
AU  - Wang, Huaichang
AU  - Cao, Jingjing
AU  - Jing, Xueyuan
AU  - Du, Yi
PY  - 2026
TI  - Multifractal Characteristics of Pore Structure in Deep Coal Reservoirs of the Suide Block, Ordos Basin
T2  - ACS Omega
DO  - 10.1021/acsomega.6c04169
UR  - https://pubs.acs.org/doi/10.1021/acsomega.6c04169
N1  - Published online 2026-07-01. Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-129-PROVISIONAL
AU  - Shao, Yan
AU  - Liu, Yu
AU  - Wang, Shaoqing
AU  - Fu, Zilong
AU  - Wang, Xiaoling
AU  - Xu, Wanglin
PY  - 2026
TI  - Linking macromolecular structure, nanopore evolution and methane adsorption in deep Ordos Basin coal: A mechanistic insight
T2  - Journal of Molecular Structure
VL  - 1364
SP  - 145895
DO  - 10.1016/j.molstruc.2026.145895
UR  - https://doi.org/10.1016/j.molstruc.2026.145895
N1  - Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-130-PROVISIONAL
AU  - Xu, Shuai
AU  - Wu, Caifang
AU  - Yang, Lei
AU  - Wang, Fangfang
AU  - Yan, Zhihua
AU  - Cheng, Yi
AU  - Zhou, Ze
PY  - 2026
TI  - Co-evolution of adsorption energetics and methane occurrence state in deep mid-to high-rank coal seams: implications for development
T2  - Physics and Chemistry of the Earth
VL  - 144
SP  - 104541
DO  - 10.1016/j.pce.2026.104541
UR  - https://doi.org/10.1016/j.pce.2026.104541
N1  - Part 2; future issue metadata. Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-131-PROVISIONAL
AU  - Ge, Tengze
AU  - Xiong, Xianyue
AU  - Li, Shuguang
AU  - Xu, Xiaohu
AU  - Gao, Ersi
AU  - Wang, Chengwang
AU  - Wang, Chuangye
AU  - Liu, Shuai-Shuai
AU  - Wei, Kai
PY  - 2026
TI  - Thermal recovery technology of deep coalbed methane: mechanisms, technologies, and development challenges
T2  - Fuel
VL  - 424
SP  - 139357
DO  - 10.1016/j.fuel.2026.139357
UR  - https://doi.org/10.1016/j.fuel.2026.139357
N1  - Future issue metadata. Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-132-PROVISIONAL
AU  - Yuan, Beijie
AU  - Zhang, Shicheng
AU  - Xiao, Cong
AU  - He, Jiayuan
PY  - 2026
TI  - Reservoir evaluation for deep coalbed methane horizontal wells based on elemental identification
T2  - Petroleum Science Bulletin
VL  - 11
IS  - 3
SP  - 819
EP  - 835
DO  - 10.3969/j.issn.2096-1693.2026.01.015
UR  - https://sykxtb.cup.edu.cn/EN/10.3969/j.issn.2096-1693.2026.01.015
N1  - Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-133-PROVISIONAL
AU  - Chen, Zhengrong
AU  - Liu, Wei
AU  - Shi, Xian
AU  - Xie, Xin
AU  - Ge, Xiaoxin
AU  - Li, Guowu
PY  - 2026
TI  - Prediction of in-situ stress field of deep coalbed methane considering coalbed structure differences
T2  - Coal Science and Technology
VL  - 54
IS  - 2
DO  - 10.12438/cst.2025-0365
UR  - https://www.mtkxjs.com.cn/article/doi/10.12438/cst.2025-0365
N1  - Conflicting page ranges require official verification before import. Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-134-PROVISIONAL
AU  - Guo, Xusheng
AU  - Liu, Zengqin
AU  - Zhao, Peirong
AU  - Shen, Baojian
AU  - Zhao, Shihu
AU  - Ye, Jincheng
AU  - Zhang, Jiaqi
AU  - Wan, Junyu
AU  - Chen, Xinjun
AU  - Qiu, Feng
AU  - Shao, Yanwen
AU  - Wang, Tianyun
AU  - Ding, Anxu
AU  - Ma, Chao
PY  - 2026
TI  - Controls of deep coalbed methane preservation conditions on enrichment and high productivity in North China
T2  - Petroleum Science Bulletin
VL  - 11
IS  - 1
SP  - 2
EP  - 13
DO  - 10.3969/j.issn.2096-1693.2026.01.001
UR  - https://sykxtb.cup.edu.cn/EN/10.3969/j.issn.2096-1693.2026.01.001
N1  - Provisional ID.
ER  -

TY  - JOUR
ID  - DCBM-135-MANUAL-REVIEW
AU  - Yang, Di
AU  - Tian, Yongjing
AU  - Fang, Maojun
AU  - Bai, Yuhu
AU  - Qi, Yu
AU  - Liu, Fen
AU  - Feng, Ruyong
AU  - Lu, Hao
PY  - 2026
TI  - Coalbed Methane Reservoir Characterization and Geological Modeling: A Case Study of Block A in the Shenfu Gas Field, Eastern Margin of the Ordos Basin
T2  - ACS Omega
DO  - 10.1021/acsomega.6c01024
UR  - https://pubs.acs.org/doi/10.1021/acsomega.6c01024
N1  - Manual review only; confirm deep-CBM inclusion boundary before import.
ER  -
```

---

# 9. BibTeX block

```bibtex
@article{Zhang2026WettabilityDeepCoalMethane,
  author  = {Zhang, Tao and Guo, Jianchun and Zhao, Zhihong and Zeng, Jie},
  title   = {Mechanism of Wettability Alteration to Unlock Adsorbed-State Methane in Deep Coal Rock: Insight from Experiment and Molecular Simulation},
  journal = {Energy \& Fuels},
  year    = {2026},
  doi     = {10.1021/acs.energyfuels.6c02337},
  url     = {https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02337}
}

@article{Chang2026DeepCoalAdsorptionThermodynamics,
  author  = {Chang, Xiangchun and Wang, Shangbin and Zhang, Junjian and Shi, Bingbing and Vandeginste, Veerle and Liu, Yu and Zhang, Pengfei},
  title   = {Adsorption Thermodynamic Property of Deep Coal Reservoirs and Adsorption Capacity Prediction under Different Temperature and Pressure Conditions},
  journal = {Energy \& Fuels},
  year    = {2026},
  doi     = {10.1021/acs.energyfuels.6c02529},
  url     = {https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02529}
}

@article{Liu2026UltrasaltSlickwaterDeepCBM,
  author  = {Liu, Pingli and Zuo, Chengwei and Du, Juan and Li, Jiahao and Zhang, Xin and Zhao, Renyin},
  title   = {Bioinspired by Mussels: Construction of an Ultrasalt-Tolerant, Tunable-Viscosity Slickwater Fracturing Fluid for the Reuse of Deep Coalbed Methane Flowback Fluids},
  journal = {Langmuir},
  year    = {2026},
  doi     = {10.1021/acs.langmuir.6c01692},
  url     = {https://pubs.acs.org/doi/10.1021/acs.langmuir.6c01692}
}

@article{Shi2026MultifractalSuideDeepCoal,
  author  = {Shi, Yunhe and Xu, Chang and Wang, Kangle and Zhang, Hui and Liang, Chen and Wang, Huaichang and Cao, Jingjing and Jing, Xueyuan and Du, Yi},
  title   = {Multifractal Characteristics of Pore Structure in Deep Coal Reservoirs of the Suide Block, Ordos Basin},
  journal = {ACS Omega},
  year    = {2026},
  doi     = {10.1021/acsomega.6c04169},
  url     = {https://pubs.acs.org/doi/10.1021/acsomega.6c04169}
}

@article{Shao2026MacromolecularNanoporeMethane,
  author  = {Shao, Yan and Liu, Yu and Wang, Shaoqing and Fu, Zilong and Wang, Xiaoling and Xu, Wanglin},
  title   = {Linking macromolecular structure, nanopore evolution and methane adsorption in deep Ordos Basin coal: A mechanistic insight},
  journal = {Journal of Molecular Structure},
  year    = {2026},
  volume  = {1364},
  pages   = {145895},
  doi     = {10.1016/j.molstruc.2026.145895}
}

@article{Xu2026AdsorptionEnergeticsDeepCoal,
  author  = {Xu, Shuai and Wu, Caifang and Yang, Lei and Wang, Fangfang and Yan, Zhihua and Cheng, Yi and Zhou, Ze},
  title   = {Co-evolution of adsorption energetics and methane occurrence state in deep mid-to high-rank coal seams: implications for development},
  journal = {Physics and Chemistry of the Earth},
  year    = {2026},
  volume  = {144},
  pages   = {104541},
  doi     = {10.1016/j.pce.2026.104541}
}

@article{Ge2026ThermalRecoveryDeepCBM,
  author  = {Ge, Tengze and Xiong, Xianyue and Li, Shuguang and Xu, Xiaohu and Gao, Ersi and Wang, Chengwang and Wang, Chuangye and Liu, Shuai-Shuai and Wei, Kai},
  title   = {Thermal recovery technology of deep coalbed methane: mechanisms, technologies, and development challenges},
  journal = {Fuel},
  year    = {2026},
  volume  = {424},
  pages   = {139357},
  doi     = {10.1016/j.fuel.2026.139357}
}

@article{Yuan2026ElementalDeepCBMEvaluation,
  author  = {Yuan, Beijie and Zhang, Shicheng and Xiao, Cong and He, Jiayuan},
  title   = {Reservoir evaluation for deep coalbed methane horizontal wells based on elemental identification},
  journal = {Petroleum Science Bulletin},
  year    = {2026},
  volume  = {11},
  number  = {3},
  pages   = {819--835},
  doi     = {10.3969/j.issn.2096-1693.2026.01.015}
}

@article{Chen2026DeepCBMStressField,
  author  = {Chen, Zhengrong and Liu, Wei and Shi, Xian and Xie, Xin and Ge, Xiaoxin and Li, Guowu},
  title   = {Prediction of in-situ stress field of deep coalbed methane considering coalbed structure differences},
  journal = {Coal Science and Technology},
  year    = {2026},
  volume  = {54},
  number  = {2},
  doi     = {10.12438/cst.2025-0365},
  note    = {Final page range requires official verification}
}

@article{Guo2026NorthChinaDeepCBMPreservation,
  author  = {Guo, Xusheng and Liu, Zengqin and Zhao, Peirong and Shen, Baojian and Zhao, Shihu and Ye, Jincheng and Zhang, Jiaqi and Wan, Junyu and Chen, Xinjun and Qiu, Feng and Shao, Yanwen and Wang, Tianyun and Ding, Anxu and Ma, Chao},
  title   = {Controls of deep coalbed methane preservation conditions on enrichment and high productivity in North China},
  journal = {Petroleum Science Bulletin},
  year    = {2026},
  volume  = {11},
  number  = {1},
  pages   = {2--13},
  doi     = {10.3969/j.issn.2096-1693.2026.01.001}
}

@article{Yang2026ShenfuCBMModelManualReview,
  author  = {Yang, Di and Tian, Yongjing and Fang, Maojun and Bai, Yuhu and Qi, Yu and Liu, Fen and Feng, Ruyong and Lu, Hao},
  title   = {Coalbed Methane Reservoir Characterization and Geological Modeling: A Case Study of Block A in the Shenfu Gas Field, Eastern Margin of the Ordos Basin},
  journal = {ACS Omega},
  year    = {2026},
  doi     = {10.1021/acsomega.6c01024},
  note    = {Manual review only; confirm deep-CBM inclusion boundary}
}
```

---

# 10. Codex 执行指令

```text
任务：处理 2026-07-22 Deep CBM Daily Brief。

一、执行前重新读取唯一正式来源

1. 00_Master/Deep_CBM_Latest.xlsx
2. 00_Master/index/Deep_CBM_master_index.jsonl
3. 00_Master/index/Deep_CBM_master_index.csv
4. 最新 06_Statistics/Master_Index_Report_*.md
5. CHANGELOG.md
6. 09_Daily_Brief/2026-07-22/Deep_CBM_daily_brief_20260722.md
7. 最近实际存在的 09_Daily_Brief 日期目录

不得仅依据本日报中的：
- master_count = 124
- last_id = DCBM-124
- provisional IDs = DCBM-125 至 DCBM-135-MR

这些值只是日报生成时的状态。

二、候选列表

建议执行时再次查重后入库：

1. 10.1021/acs.energyfuels.6c02337
2. 10.1021/acs.energyfuels.6c02529
3. 10.1021/acs.langmuir.6c01692
4. 10.1021/acsomega.6c04169
5. 10.1016/j.molstruc.2026.145895
6. 10.1016/j.pce.2026.104541
7. 10.1016/j.fuel.2026.139357
8. 10.3969/j.issn.2096-1693.2026.01.015
9. 10.12438/cst.2025-0365
10. 10.3969/j.issn.2096-1693.2026.01.001

仅人工复核，不得自动入库：

11. 10.1021/acsomega.6c01024

三、逐条去重

对每个候选依次执行：

1. DOI_normalized 完全匹配；
2. 英文题名_normalized 完全匹配；
3. 中文题名_normalized 完全匹配；
4. 第一作者 + 年份 + 严格题名相似性；
5. Online First、Early Access、预出版和正式卷期版本合并检查；
6. 最近 Daily Brief 是否已推荐同一候选；
7. 同一论文的中英文题名和不同数据库版本人工核对。

如发现重复：

- 跳过该候选；
- 记录 duplicate reason；
- 记录 matched field；
- 记录 existing DCBM ID；
- 记录 existing DOI、英文题名和中文题名；
- 不占用新编号；
- 继续处理其余非重复候选。

四、已知重复项，必须跳过

- 10.1016/j.engeos.2026.100609 = DCBM-115
- 10.13225/j.cnki.jccs.QH25.0479 = DCBM-121
- 10.1038/s41598-026-54924-z = DCBM-119
- 10.3389/feart.2026.1772109 = DCBM-028

五、元数据特别处理

Candidate 4，DOI 10.1021/acsomega.6c04169：
- 摘要和结论中的微孔比例存在 86.26% 与 87.78% 的源内差异；
- 不得擅自统一或改写；
- 可在精读摘要中注明来源位置差异。

Candidate 6 和 Candidate 7：
- 属于已在线但正式期次日期在未来的记录；
- 不得写成尚未发表的预印本；
- 应准确记录 online publication 状态和未来卷期信息。

Candidate 9，DOI 10.12438/cst.2025-0365：
- 官方 HTML 和 PDF/检索片段出现 360–369 与 375–384 两组页码；
- 必须读取最终 PDF 首页或期刊正式引用格式解决冲突；
- 冲突未解决前不得正式写入页码字段；
- 在 update log 中记录 metadata conflict resolution。

Candidate 11，DOI 10.1021/acsomega.6c01024：
- 仅 manual_review_only；
- 必须确认研究层位埋深及是否符合知识库深部煤层气纳入标准；
- 未通过人工相关性复核前不得写入主表；
- 不占用最终 DCBM 编号。

六、最终编号

- 本日报全部编号均为 provisional。
- 读取执行时当前最后一个实际 DCBM ID。
- 仅对确认非重复、元数据完整且允许正式入库的候选连续编号。
- 重复候选和 manual_review_only 候选不占用编号。
- 不产生编号空洞。
- 不重新编号已有记录。

七、正式写入与派生文件

仅对通过去重和元数据核验的候选：

1. 更新 00_Master/Deep_CBM_Latest.xlsx；
2. 保留全部既有 sheet、字段、格式、公式、超链接、批注和人工内容；
3. 创建新的 master snapshot，不覆盖历史 snapshot；
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

八、QC 要求

至少验证：

- 主工作簿可正常打开；
- 第一张 sheet 仍为完整文献矩阵；
- 8 个活动 sheet 均保留；
- 文献 ID 唯一且连续；
- DOI_normalized 重复数为 0；
- 英文题名_normalized 重复数为 0；
- 中文题名_normalized 重复数为 0；
- 主工作簿记录数与 JSONL、CSV 一致；
- increment Excel、RIS、BibTeX 和 DOI list 数量一致；
- skipped duplicate 包含原因和 existing ID；
- manual_review_only 未误写入主表；
- 所有在线优先和未来卷期状态记录准确；
- 元数据冲突已记录解决过程；
- CHANGELOG 与实际新增数一致；
- 保护目录未修改。

九、保护范围

严格禁止修改：

- 08_User/
- 00_Master/source/
- 00_Master/workbook_archive/
- 已存在的 snapshot
- 已存在的历史 increment
- 用户阅读标记
- 用户批注
- 用户自定义字段
- 用户人工排序

十、最终汇报字段

输出：

- status
- action
- master_count_before
- master_count_after
- last_id_before
- last_id_after
- candidate_count
- added_count
- duplicate_skipped_count
- manual_review_count
- final_assigned_ids
- duplicate_skipped_details
- metadata_conflict_resolution
- official_metadata_verified
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

# 11. Daily ingest manifest

```json
{
  "brief_date": "2026-07-22",
  "brief_type": "candidate_update",
  "repository_source_of_truth_checked": true,
  "master_status_at_check": {
    "record_count": 124,
    "last_id": "DCBM-124",
    "id_continuous": true,
    "doi_missing_count": 1,
    "doi_duplicate_count": 0,
    "english_title_duplicate_count": 0,
    "chinese_title_duplicate_count": 0,
    "last_formal_update": "2026-07-10"
  },
  "recommended_add_count": 10,
  "manual_review_count": 1,
  "known_duplicate_count": 4,
  "provisional_ids": [
    "DCBM-125",
    "DCBM-126",
    "DCBM-127",
    "DCBM-128",
    "DCBM-129",
    "DCBM-130",
    "DCBM-131",
    "DCBM-132",
    "DCBM-133",
    "DCBM-134",
    "DCBM-135-MR"
  ],
  "codex_action": "preflight_then_apply_verified_nonduplicates_only",
  "direct_repository_edit_performed": false,
  "protected_directory_edit_performed": false
}
```

---

# 12. 最终状态

```text
daily_brief_status: 10_recommended_candidates_plus_1_manual_review
repository_source_of_truth_checked: yes
master_record_count_at_check: 124
last_master_id_at_check: DCBM-124
recommended_add_count: 10
manual_review_count: 1
known_duplicate_count: 4
master_workbook_change_needed: pending_codex_live_deduplication
direct_repository_edit_performed: no
protected_directory_edit_performed: no
```
