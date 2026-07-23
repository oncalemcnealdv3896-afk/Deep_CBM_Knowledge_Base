# Deep CBM Knowledge Base Daily Brief — 2026-07-23

> 建议保存路径：`09_Daily_Brief/2026-07-23/Deep_CBM_daily_brief_20260723.md`

## 1. 今日结论

本轮首先读取 GitHub 仓库 `oncalemcnealdv3896-afk/Deep_CBM_Knowledge_Base`，并将以下文件作为唯一正式事实来源：

- `00_Master/index/Deep_CBM_master_index.jsonl`
- `00_Master/index/Deep_CBM_master_index.csv`
- `06_Statistics/Master_Index_Report_20260710.md`
- `CHANGELOG.md`
- 仓库最新提交记录及 `09_Daily_Brief/` 可检索文件

当前正式主库仍为 **124 条、最后编号 DCBM-124**；ID 连续，DOI及中英文题名重复数均为 0。仓库没有 2026-07-10 之后的正式提交，且预期的 2026-07-10 日报路径当前返回 404，因此本轮不把聊天中生成但未提交仓库的日报视为正式状态。

经官方期刊页、出版商页面和 DOI 记录检索，并按 DOI、题名及第一作者—年份去重，本轮得到：

- **建议 Codex 实时复核后入库：10 篇**
- **仅人工复核：3 篇**
- **确认重复并排除：5 篇**
- **未直接修改 Excel、RIS、BibTeX 或仓库**

暂定编号 DCBM-125—DCBM-134；人工复核项标记为 DCBM-135-MR—DCBM-137-MR。所有编号均为 provisional，最终必须由 Codex 按执行时最新主库连续重排。

## 2. 当前主库状态

| 项目 | 当前值 |
|---|---:|
| 主工作簿 | `00_Master/Deep_CBM_Latest.xlsx` |
| 记录数 | 124 |
| 最后编号 | DCBM-124 |
| ID 连续 | 是 |
| DOI 缺失 | 1 |
| DOI 重复 | 0 |
| 英文题名重复 | 0 |
| 中文题名重复 | 0 |
| 最近正式更新 | 2026-07-10 |
| 最新提交 | `48f61d23f87d7e4f702dc2815f82c5591159c0dc` |

2026-07-10 更新新增 DCBM-122—DCBM-124，并重建索引、QC 和增量文件；`08_User/`、`00_Master/source/`、`00_Master/workbook_archive/` 未修改。

## 3. 检索范围与去重

- 检索日期：2026-07-23
- 重点窗口：2026-07-10—2026-07-23
- 补充范围：2026 年近期正式卷期、Online First、近期 DOI 注册或近期可发现的高相关文献
- 主题：deep coalbed methane、deep CBM、deep coal-rock gas、deep coal measures gas、见气时间、排采、吸附/游离气、润湿性、水锁、压裂示踪、全域支撑、纳米限域
- 优先来源：《煤炭学报》、ACS、ScienceDirect、MDPI、正式 DOI 页面及主要数据库

去重顺序：DOI_normalized → 英文题名_normalized → 中文题名_normalized → 第一作者—年份—题名 → Online First/正式卷期合并 → 人工语义复核。

# 4. 建议正式候选

## DCBM-125 provisional

**深部煤层气井见气时间控制机理与排采制度优化**  
英文：*Mechanism of gas breakthrough time control in deep CBM wells and optimization of production strategies*  
XI Zhaodong; TANG Shuheng; DUAN Lijiang; ZHANG Songhang; WANG Zhizhen.  
《煤炭学报》2026, 51(2):1463–1475. DOI: `10.13225/j.cnki.jccs.XH25.1256`  
官方页：`https://www.mtxb.com.cn/article/doi/10.13225/j.cnki.jccs.XH25.1256`  
**优先级：A+**

- 研究区：鄂尔多斯盆地东缘北部；百余口井地质和动态资料。
- 方法：见气饱和度、状态方程、Langmuir、气水两相渗流、实验和 COMET3 模拟。
- 发现：见气时间 0–276 d，平均 30.6 d；研究区单相排水阶段合理压降速率 0.10–0.25 MPa/d；典型井模拟见气时间缩短 8%–80%，平均日产气提高 5.9%–11.8%。
- 创新：定量连接游离气富集、压降和首次见气。
- 局限：模式和压降区间具有区块适用性，不得反向用于用户项目正式分型或最优制度。
- 建议引用：引言、首次见气对齐方法、压力传播/解吸讨论、局限。
- 去重：当前索引无 DOI/题名匹配；与 DCBM-114 为同作者同年份不同论文。

## DCBM-126 provisional

**准噶尔盆地深部煤层气勘探开发进展及前景展望**  
英文：*Progress and prospect of exploration and development of deep coalbed methane in the Junggar Basin*  
QIU Peng 等 9 人.《煤炭学报》2026, 51(S1):299–312. DOI: `10.13225/j.cnki.jccs.2025.0522`  
官方页：`https://www.mtxb.com.cn/article/doi/10.13225/j.cnki.jccs.2025.0522`  
**优先级：A**

- 对象：准噶尔盆地侏罗系中低煤阶深部煤层气。
- 方法：盆地尺度地质、含气性、成藏、压裂和水平井动态综合。
- 发现：吸附气临界深度约 1000–1500 m，总含气量临界深度约 2500–3000 m；2000 m 后游离气比例可接近 50%；水平井常见气快、产水和返排率低，早中期游离气、后期吸附气贡献增强。
- 创新：提供中低煤阶、强润湿性盆地案例。
- 局限：深度阈值和压裂体系不可直接外推。
- 建议引用：盆地进展、游离/吸附气、返排与液相滞留、区域差异。
- 去重：索引无 DOI/题名匹配；非已有白家海个案论文的重复。

## DCBM-127 provisional

*Mechanism of Wettability Alteration to Unlock Adsorbed-State Methane in Deep Coal Rock: Insight from Experiment and Molecular Simulation*  
Tao Zhang; Jianchun Guo; Zhihong Zhao; Jie Zeng. Energy & Fuels, online 2026-07-10. DOI: `10.1021/acs.energyfuels.6c02337`  
官方页：`https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02337`  
建议中文题名：**深部煤岩润湿性调控促进吸附态甲烷释放机理**  
**优先级：A+**

- 方法：渗吸、孔隙表征、吸附/解吸和分子动力学。
- 发现：0.3–1.5 nm 孔尺度增加 59.6%，2–10 nm 增加 44.8%；CH₄—煤配位数 16.2→12.3，水—煤 0→9.6；模拟能垒约 1500→800 kJ/mol。
- 创新：统一解释润湿性、孔隙重构和水膜竞争吸附。
- 局限：微观和实验结果不能直接证明井级长期增产。
- 相关性：水锁、液相滞留、解吸启动、裂缝—基质传质。
- 去重：索引未检出 DOI或题名。

## DCBM-128 provisional

*Adsorption Thermodynamic Property of Deep Coal Reservoirs and Adsorption Capacity Prediction under Different Temperature and Pressure Conditions*  
Xiangchun Chang 等 7 人. Energy & Fuels, online 2026-07-10. DOI: `10.1021/acs.energyfuels.6c02529`  
官方页：`https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c02529`  
建议中文题名：**深部煤储层吸附热力学性质及不同温压条件下吸附容量预测**  
**优先级：A−**

- 数据：鄂尔多斯东缘本溪组 3 口井、17 件煤样。
- 方法：工业分析、CO₂ 吸附、高温高压甲烷吸附、等量吸附热和模型预测。
- 发现：灰分总体削弱微孔和吸附，固定碳/微孔与 Langmuir 体积正相关；升温降低吸附，升压提高吸附。
- 局限：模型受煤阶和实验温压范围约束，吸附容量不等于可采气量。
- 相关性：温压背景、吸附/游离气和资料边界。
- 去重：索引未检出 DOI或题名。

## DCBM-129 provisional

*Bioinspired by Mussels: Construction of an Ultrasalt-Tolerant, Tunable-Viscosity Slickwater Fracturing Fluid for the Reuse of Deep Coalbed Methane Flowback Fluids*  
Pingli Liu 等 6 人. Langmuir, online 2026-07-14. DOI: `10.1021/acs.langmuir.6c01692`  
官方页：`https://pubs.acs.org/doi/10.1021/acs.langmuir.6c01692`  
建议中文题名：**贻贝仿生超耐盐可调黏滑溜水压裂液及返排液回用**  
**优先级：A−**

- 方法：超高矿化度配伍、流变、减阻、携砂、破胶、残渣和分子模拟。
- 发现：TDS >120,000 mg/L 时黏度约 75 mPa·s；最大减阻率 79.58%；60 ℃ 约 3 h 破胶，残渣约 310 mg/L。
- 创新：整合返排液回用、耐盐、减阻和携砂。
- 局限：材料性能不能直接证明产气提升，需现场地层伤害验证。
- 相关性：返排、水锁、液相滞留和压裂液差异。
- 去重：索引未检出 DOI或题名。


## DCBM-130 provisional

*Multifractal Characteristics of Pore Structure in Deep Coal Reservoirs of the Suide Block, Ordos Basin*  
Yunhe Shi 等 9 人. ACS Omega, online 2026-07-01. DOI: `10.1021/acsomega.6c04169`  
官方页：`https://pubs.acs.org/doi/10.1021/acsomega.6c04169`  
建议中文题名：**绥德区块深部煤储层孔隙结构多重分形特征**  
**优先级：A−**

- 对象：本溪组 8 号深部煤。
- 方法：FESEM、低温 CO₂/N₂ 吸附、高压压汞和多重分形。
- 发现：微孔约占 86.26%；各级孔隙均多重分形；大孔非均质性最高、连通性最差；灰分降低孔容并削弱中大孔连通。
- 局限：样本量有限，分形参数与井级产能缺乏跨尺度验证。
- 相关性：微孔吸附、中大孔渗流、裂缝—基质传质。
- 去重：索引未检出 DOI或题名。

## DCBM-131 provisional

*Fracturing Tracer Monitoring and Machine Learning-Assisted Geology-Engineering Coupled Optimization for Deep Coalbed Methane Horizontal Wells*  
Hong Zhuo; Zhangying Han; Shaohua Li; Xiuling He; Demei Zhang; Haibin Song; Gang Hui. Processes 2026, 14(12):1890. DOI: `10.3390/pr14121890`  
官方页：`https://www.mdpi.com/2227-9717/14/12/1890`  
建议中文题名：**深部煤层气水平井压裂示踪监测与机器学习辅助地质—工程耦合优化**  
**优先级：A**

- 数据：长庆矿区 10 口井、132 个压裂段；8 口完整井 105 段用于主分析，2 口井 27 段用于独立验证。
- 方法：水相/气相示踪、Pearson、Random Forest 和段级生产贡献解释。
- 发现：外部研究识别 3 种段间产出形态；一类煤钻遇长度与初始产气的幂律 R²=0.71；保留测试集 R²=0.83；提出差异化压裂窗口。
- 创新：把段级示踪、生产剖面和机器学习闭环结合。
- 局限：外部分类和特征重要性不得变成用户项目正式类型或主控因素排序。
- 建议引用：压裂差异、段间非均质性、独立监测资料缺口、exploratory ML 边界。
- 去重：索引未检出 DOI或题名。

## DCBM-132 provisional

**煤岩气全域支撑压裂的几个关键问题与思考**  
英文：*Several key issues and insights in full-scale proppant-support fracturing for deep coal rock gas formations*  
GUO Jianchun 等 10 人.《煤炭学报》2026, 51(1):613–629. DOI: `10.13225/j.cnki.jccs.2025.1460`  
官方页：`https://www.mtxb.com.cn/article/doi/10.13225/j.cnki.jccs.2025.1460`  
**优先级：A**

- 提出“点解吸、线疏通、面促缝、体支撑”理念。
- 讨论基质孔隙改造、渗吸置换、割理激活、长缝网、多级缝宽—支撑剂匹配以及主缝/层理缝/割理缝全域支撑。
- 创新：从吸附气—游离气连续供气角度连接基质、割理和人工裂缝。
- 局限：以理论和工程思考为主，不能替代用户项目压裂施工、示踪或导流能力资料。
- 建议引用：压裂导流、裂缝网络、连续供气、压裂改造差异。
- 去重：索引未检出 DOI或题名。

## DCBM-133 provisional

*Mechanisms of deep coalbed methane occurrence: Review and perspectives*  
Sihao Li; Xin Li; Yong Tang; Yanpeng Chen; Jonathan Atuquaye Quaye; Chenlin Hu. Advances in Geo-Energy Research 2026, 21(1):42–59.  
官方页：`https://ager.yandypress.com/index.php/2207-9963/article/view/871`  
DOI：官方可访问页面当前未显示。  
建议中文题名：**深部煤层气赋存机理：研究进展与展望**  
**优先级：A−**

- 综述成因、埋藏演化、温压应力、吸附/游离气、构造盖层、水动力封闭、裂缝渗流和基质扩散。
- 主要认识：热成因气重要；游离气比例通常随深度增加；构造、盖层和裂缝共同控制保存和富集。
- 创新：尝试整合临界深度、裂缝渗流—基质扩散及生产模型。
- 局限：综述不能替代项目证据；不得编造 DOI。
- 去重：索引无题名匹配；Codex 必须按题名—作者—年份—卷期联合复核。

## DCBM-134 provisional

*Nanoconfinement effects on adsorbed and free methane densities: Revisiting coalbed methane content evaluation*  
Wei Yang; Yanbin Yao; Dong Feng; Xiaoxiao Sun; Zefan Wang; Shulei Duan. Fuel 427, Part C, 139801. DOI: `10.1016/j.fuel.2026.139801`  
官方页：`https://www.sciencedirect.com/science/article/pii/S0016236126015553`  
正式卷期日期：2027-01-01；DOI和在线元数据在 2026 年已注册。  
建议中文题名：**纳米限域对吸附态与游离态甲烷密度的影响：煤层气含量评价再认识**  
**优先级：A**

- 方法：狭缝纳米孔模拟、Peng–Robinson 状态方程修正、限域逸度—压力、吸附相/游离相密度和煤阶修正。
- 发现：以体相密度处理纳米孔会系统偏置吸附/游离气分配；忽略限域可能低估深部煤层中的真实游离气比例。
- 创新：把孔隙尺度限域热力学传递到储层含气量评价。
- 局限：依赖孔形、状态方程和煤阶修正，需保压取心和现场数据验证。
- 相关性：早期游离气贡献和相态评价边界。
- 去重：索引未检出 DOI或题名。

# 5. 仅人工复核候选

## DCBM-135-MR

- DOI：`10.1021/acsomega.6c01024`
- 题名：*Coalbed Methane Reservoir Characterization and Geological Modeling: A Case Study of Block A in the Shenfu Gas Field, Eastern Margin of the Ordos Basin*
- 第一作者：Di Yang；ACS Omega；online 2026-07-17。
- 内容：宏观煤岩类型、储层表征和三维地质建模。
- 暂缓原因：题名未明确 deep，需核实目标层埋深和知识库纳入边界。
- 转正条件：全文明确符合深部定义，且执行时 DOI/题名仍不重复。

## DCBM-136-MR

- DOI：`10.1021/acsomega.6c04752`
- 题名：*Pore Structure Reconstruction and Gas–Water Dual-Flow Simulations Combined with CT Scans and NMR Measurements on Coal Particle Samples*
- 第一作者：Mingjun Zou；ACS Omega；online 2026-07-15。
- 内容：CT、NMR、孔隙重构和气水两相模拟。
- 暂缓原因：公开矿井埋深约 800–1200 m，可能不符合当前油气型深部煤层气边界。
- 转正条件：人工决定是否纳入“方法参考层”，并显式标注深度口径。

## DCBM-137-MR

- DOI：`10.1021/acsomega.6c05059`
- 题名：*Experimental and Numerical Study on Gas-Displacing-Water in Coal Reservoirs under Different Confining Pressures Using LF-NMR*
- 第一作者：Kaide Liu；ACS Omega；online 2026-07-09。
- 内容：低场核磁、不同围压气驱水和热—流—固模拟。
- 暂缓原因：煤层埋深约 800–850 m；作者的“深部”矿井口径与知识库常用 >1500 m 口径不一致。
- 转正条件：人工确认仅作为机制方法文献纳入。

# 6. 已确认重复并排除

| DOI | 已有 ID | 排除原因 |
|---|---|---|
| `10.1016/j.engeos.2026.100609` | DCBM-115 | DOI和英文题名完全匹配 |
| `10.1038/s41598-026-54924-z` | DCBM-119 | DOI和题名完全匹配 |
| `10.13225/j.cnki.jccs.QH25.0479` | DCBM-121 | DOI和题名完全匹配 |
| `10.3389/feart.2026.1772109` | DCBM-028 | CHANGELOG 已记录重复 |
| `10.1021/acs.energyfuels.5c06267` | DCBM-021 | DOI完全匹配 |

# 7. Matrix-ready rows

| provisional_id | recommendation | DOI | 英文题名 | 第一作者 | 年份 | 来源 | 卷期/文章号 | 核验状态 | 优先级 |
|---|---|---|---|---|---:|---|---|---|---|
| DCBM-125 | add_after_live_dedup | 10.13225/j.cnki.jccs.XH25.1256 | Mechanism of gas breakthrough time control in deep CBM wells and optimization of production strategies | XI Zhaodong | 2026 | Journal of China Coal Society | 51(2):1463–1475 | 官方完整核验 | A+ |
| DCBM-126 | add_after_live_dedup | 10.13225/j.cnki.jccs.2025.0522 | Progress and prospect of exploration and development of deep coalbed methane in the Junggar Basin | QIU Peng | 2026 | Journal of China Coal Society | 51(S1):299–312 | 官方完整核验 | A |
| DCBM-127 | add_after_live_dedup | 10.1021/acs.energyfuels.6c02337 | Mechanism of Wettability Alteration to Unlock Adsorbed-State Methane in Deep Coal Rock | Tao Zhang | 2026 | Energy & Fuels | Online | ACS核验 | A+ |
| DCBM-128 | add_after_live_dedup | 10.1021/acs.energyfuels.6c02529 | Adsorption Thermodynamic Property of Deep Coal Reservoirs and Adsorption Capacity Prediction | Xiangchun Chang | 2026 | Energy & Fuels | Online | ACS核验 | A− |
| DCBM-129 | add_after_live_dedup | 10.1021/acs.langmuir.6c01692 | Bioinspired Ultrasalt-Tolerant Slickwater for Deep CBM Flowback Reuse | Pingli Liu | 2026 | Langmuir | Online | ACS核验 | A− |
| DCBM-130 | add_after_live_dedup | 10.1021/acsomega.6c04169 | Multifractal Characteristics of Pore Structure in Deep Coal Reservoirs of the Suide Block | Yunhe Shi | 2026 | ACS Omega | Online | ACS核验 | A− |
| DCBM-131 | add_after_live_dedup | 10.3390/pr14121890 | Fracturing Tracer Monitoring and ML-Assisted Optimization for Deep CBM Horizontal Wells | Hong Zhuo | 2026 | Processes | 14(12):1890 | MDPI核验 | A |
| DCBM-132 | add_after_live_dedup | 10.13225/j.cnki.jccs.2025.1460 | Several key issues and insights in full-scale proppant-support fracturing | GUO Jianchun | 2026 | Journal of China Coal Society | 51(1):613–629 | 官方完整核验 | A |
| DCBM-133 | add_after_title_author_year_dedup | 待核验 | Mechanisms of deep coalbed methane occurrence: Review and perspectives | Sihao Li | 2026 | Advances in Geo-Energy Research | 21(1):42–59 | DOI待核验 | A− |
| DCBM-134 | add_after_live_dedup | 10.1016/j.fuel.2026.139801 | Nanoconfinement effects on adsorbed and free methane densities | Wei Yang | 2027 issue | Fuel | 427 Part C:139801 | 出版商/Crossref核验 | A |
| DCBM-135-MR | manual_review_only | 10.1021/acsomega.6c01024 | Coalbed Methane Reservoir Characterization and Geological Modeling | Di Yang | 2026 | ACS Omega | Online | 深部相关性待审 | B+ |
| DCBM-136-MR | manual_review_only | 10.1021/acsomega.6c04752 | Pore Structure Reconstruction and Gas–Water Dual-Flow Simulations | Mingjun Zou | 2026 | ACS Omega | Online | 埋深边界待审 | B |
| DCBM-137-MR | manual_review_only | 10.1021/acsomega.6c05059 | Gas-Displacing-Water under Different Confining Pressures Using LF-NMR | Kaide Liu | 2026 | ACS Omega | Online | 深度口径待审 | B+ |


# 8. RIS block

```ris
TY  - JOUR
ID  - DCBM-125-PROVISIONAL
AU  - Xi, Zhaodong
AU  - Tang, Shuheng
AU  - Duan, Lijiang
AU  - Zhang, Songhang
AU  - Wang, Zhizhen
PY  - 2026
TI  - Mechanism of gas breakthrough time control in deep CBM wells and optimization of production strategies
T2  - Journal of China Coal Society
VL  - 51
IS  - 2
SP  - 1463
EP  - 1475
DO  - 10.13225/j.cnki.jccs.XH25.1256
ER  -

TY  - JOUR
ID  - DCBM-126-PROVISIONAL
AU  - Qiu, Peng
AU  - Chen, Heqing
AU  - Yang, Zhaobiao
AU  - Zhong, Junbing
AU  - Liu, Changqing
AU  - Li, Cunlei
AU  - Zhang, Baoxin
AU  - Liang, Yuhui
AU  - Wang, Yuqiang
PY  - 2026
TI  - Progress and prospect of exploration and development of deep coalbed methane in the Junggar Basin
T2  - Journal of China Coal Society
VL  - 51
IS  - S1
SP  - 299
EP  - 312
DO  - 10.13225/j.cnki.jccs.2025.0522
ER  -

TY  - JOUR
ID  - DCBM-127-PROVISIONAL
AU  - Zhang, Tao
AU  - Guo, Jianchun
AU  - Zhao, Zhihong
AU  - Zeng, Jie
PY  - 2026
TI  - Mechanism of Wettability Alteration to Unlock Adsorbed-State Methane in Deep Coal Rock: Insight from Experiment and Molecular Simulation
T2  - Energy & Fuels
DO  - 10.1021/acs.energyfuels.6c02337
ER  -

TY  - JOUR
ID  - DCBM-128-PROVISIONAL
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
ER  -

TY  - JOUR
ID  - DCBM-129-PROVISIONAL
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
ER  -

TY  - JOUR
ID  - DCBM-130-PROVISIONAL
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
ER  -

TY  - JOUR
ID  - DCBM-131-PROVISIONAL
AU  - Zhuo, Hong
AU  - Han, Zhangying
AU  - Li, Shaohua
AU  - He, Xiuling
AU  - Zhang, Demei
AU  - Song, Haibin
AU  - Hui, Gang
PY  - 2026
TI  - Fracturing Tracer Monitoring and Machine Learning-Assisted Geology-Engineering Coupled Optimization for Deep Coalbed Methane Horizontal Wells
T2  - Processes
VL  - 14
IS  - 12
SP  - 1890
DO  - 10.3390/pr14121890
ER  -

TY  - JOUR
ID  - DCBM-132-PROVISIONAL
AU  - Guo, Jianchun
AU  - Zeng, Jie
AU  - Zhao, Zhihong
AU  - Lu, Qianli
AU  - Zhou, Hangyu
AU  - Ren, Wenxi
AU  - Zhang, Tao
AU  - Liu, Yuxuan
AU  - Zhang, Tao
AU  - Wu, Tianyu
PY  - 2026
TI  - Several key issues and insights in full-scale proppant-support fracturing for deep coal rock gas formations
T2  - Journal of China Coal Society
VL  - 51
IS  - 1
SP  - 613
EP  - 629
DO  - 10.13225/j.cnki.jccs.2025.1460
ER  -

TY  - JOUR
ID  - DCBM-133-PROVISIONAL
AU  - Li, Sihao
AU  - Li, Xin
AU  - Tang, Yong
AU  - Chen, Yanpeng
AU  - Quaye, Jonathan Atuquaye
AU  - Hu, Chenlin
PY  - 2026
TI  - Mechanisms of deep coalbed methane occurrence: Review and perspectives
T2  - Advances in Geo-Energy Research
VL  - 21
IS  - 1
SP  - 42
EP  - 59
N1  - DOI requires verification.
ER  -

TY  - JOUR
ID  - DCBM-134-PROVISIONAL
AU  - Yang, Wei
AU  - Yao, Yanbin
AU  - Feng, Dong
AU  - Sun, Xiaoxiao
AU  - Wang, Zefan
AU  - Duan, Shulei
PY  - 2027
TI  - Nanoconfinement effects on adsorbed and free methane densities: Revisiting coalbed methane content evaluation
T2  - Fuel
VL  - 427
IS  - Part C
SP  - 139801
DO  - 10.1016/j.fuel.2026.139801
N1  - DOI registered/online metadata in 2026; formal issue dated 2027-01-01.
ER  -
```

# 9. BibTeX block

```bibtex
@article{Xi2026GasBreakthroughDeepCBM,
  author={Xi, Zhaodong and Tang, Shuheng and Duan, Lijiang and Zhang, Songhang and Wang, Zhizhen},
  title={Mechanism of gas breakthrough time control in deep CBM wells and optimization of production strategies},
  journal={Journal of China Coal Society}, year={2026}, volume={51}, number={2},
  pages={1463--1475}, doi={10.13225/j.cnki.jccs.XH25.1256}
}

@article{Qiu2026JunggarDeepCBM,
  author={Qiu, Peng and Chen, Heqing and Yang, Zhaobiao and Zhong, Junbing and Liu, Changqing and Li, Cunlei and Zhang, Baoxin and Liang, Yuhui and Wang, Yuqiang},
  title={Progress and prospect of exploration and development of deep coalbed methane in the Junggar Basin},
  journal={Journal of China Coal Society}, year={2026}, volume={51}, number={S1},
  pages={299--312}, doi={10.13225/j.cnki.jccs.2025.0522}
}

@article{Zhang2026WettabilityDeepCoal,
  author={Zhang, Tao and Guo, Jianchun and Zhao, Zhihong and Zeng, Jie},
  title={Mechanism of Wettability Alteration to Unlock Adsorbed-State Methane in Deep Coal Rock: Insight from Experiment and Molecular Simulation},
  journal={Energy \& Fuels}, year={2026}, doi={10.1021/acs.energyfuels.6c02337}
}

@article{Chang2026AdsorptionThermodynamics,
  author={Chang, Xiangchun and Wang, Shangbin and Zhang, Junjian and Shi, Bingbing and Vandeginste, Veerle and Liu, Yu and Zhang, Pengfei},
  title={Adsorption Thermodynamic Property of Deep Coal Reservoirs and Adsorption Capacity Prediction under Different Temperature and Pressure Conditions},
  journal={Energy \& Fuels}, year={2026}, doi={10.1021/acs.energyfuels.6c02529}
}

@article{Liu2026UltrasaltSlickwater,
  author={Liu, Pingli and Zuo, Chengwei and Du, Juan and Li, Jiahao and Zhang, Xin and Zhao, Renyin},
  title={Bioinspired by Mussels: Construction of an Ultrasalt-Tolerant, Tunable-Viscosity Slickwater Fracturing Fluid for the Reuse of Deep Coalbed Methane Flowback Fluids},
  journal={Langmuir}, year={2026}, doi={10.1021/acs.langmuir.6c01692}
}

@article{Shi2026MultifractalSuide,
  author={Shi, Yunhe and Xu, Chang and Wang, Kangle and Zhang, Hui and Liang, Chen and Wang, Huaichang and Cao, Jingjing and Jing, Xueyuan and Du, Yi},
  title={Multifractal Characteristics of Pore Structure in Deep Coal Reservoirs of the Suide Block, Ordos Basin},
  journal={ACS Omega}, year={2026}, doi={10.1021/acsomega.6c04169}
}

@article{Zhuo2026TracerMLDeepCBM,
  author={Zhuo, Hong and Han, Zhangying and Li, Shaohua and He, Xiuling and Zhang, Demei and Song, Haibin and Hui, Gang},
  title={Fracturing Tracer Monitoring and Machine Learning-Assisted Geology-Engineering Coupled Optimization for Deep Coalbed Methane Horizontal Wells},
  journal={Processes}, year={2026}, volume={14}, number={12}, pages={1890},
  doi={10.3390/pr14121890}
}

@article{Guo2026FullScaleProppant,
  author={Guo, Jianchun and Zeng, Jie and Zhao, Zhihong and Lu, Qianli and Zhou, Hangyu and Ren, Wenxi and Zhang, Tao and Liu, Yuxuan and Zhang, Tao and Wu, Tianyu},
  title={Several key issues and insights in full-scale proppant-support fracturing for deep coal rock gas formations},
  journal={Journal of China Coal Society}, year={2026}, volume={51}, number={1},
  pages={613--629}, doi={10.13225/j.cnki.jccs.2025.1460}
}

@article{Li2026DeepCBMOccurrenceReview,
  author={Li, Sihao and Li, Xin and Tang, Yong and Chen, Yanpeng and Quaye, Jonathan Atuquaye and Hu, Chenlin},
  title={Mechanisms of deep coalbed methane occurrence: Review and perspectives},
  journal={Advances in Geo-Energy Research}, year={2026}, volume={21}, number={1},
  pages={42--59}, note={DOI requires official verification}
}

@article{Yang2027NanoconfinementMethane,
  author={Yang, Wei and Yao, Yanbin and Feng, Dong and Sun, Xiaoxiao and Wang, Zefan and Duan, Shulei},
  title={Nanoconfinement effects on adsorbed and free methane densities: Revisiting coalbed methane content evaluation},
  journal={Fuel}, year={2027}, volume={427}, pages={139801},
  doi={10.1016/j.fuel.2026.139801},
  note={Online metadata registered in 2026; formal issue 2027-01-01}
}
```


# 10. Codex 执行指令

```text
任务：处理 2026-07-23 Deep CBM Daily Brief。

一、执行前重新读取唯一正式来源

1. 00_Master/Deep_CBM_Latest.xlsx
2. 00_Master/index/Deep_CBM_master_index.jsonl
3. 00_Master/index/Deep_CBM_master_index.csv
4. 最新 06_Statistics/Master_Index_Report_*.md
5. CHANGELOG.md
6. 09_Daily_Brief/2026-07-23/Deep_CBM_daily_brief_20260723.md
7. 最近实际存在的 09_Daily_Brief 日期目录

不得仅依据本日报中的 record_count=124、last_id=DCBM-124 或 provisional IDs。

二、候选

正式候选：
1. 10.13225/j.cnki.jccs.XH25.1256
2. 10.13225/j.cnki.jccs.2025.0522
3. 10.1021/acs.energyfuels.6c02337
4. 10.1021/acs.energyfuels.6c02529
5. 10.1021/acs.langmuir.6c01692
6. 10.1021/acsomega.6c04169
7. 10.3390/pr14121890
8. 10.13225/j.cnki.jccs.2025.1460
9. 无已确认 DOI：Mechanisms of deep coalbed methane occurrence: Review and perspectives
10. 10.1016/j.fuel.2026.139801

人工复核：
11. 10.1021/acsomega.6c01024
12. 10.1021/acsomega.6c04752
13. 10.1021/acsomega.6c05059

三、逐条去重

依次检查：
1. DOI_normalized；
2. 英文题名_normalized；
3. 中文题名_normalized；
4. 第一作者—年份—严格题名相似性；
5. Online First、Journal Pre-proof、Early Access 与正式卷期合并；
6. 最近 Daily Brief 是否已推荐；
7. 中英文版本是否为同一论文；
8. 无 DOI 文献按题名、作者、年份、期刊、卷期页码联合判断。

重复时：
- 跳过；
- 记录 duplicate reason 和 matched field；
- 记录 existing DCBM ID、DOI及题名；
- 不占用最终编号；
- 继续处理其他非重复候选。

四、已知重复，必须跳过

- 10.1016/j.engeos.2026.100609 = DCBM-115
- 10.1038/s41598-026-54924-z = DCBM-119
- 10.13225/j.cnki.jccs.QH25.0479 = DCBM-121
- 10.3389/feart.2026.1772109 = DCBM-028
- 10.1021/acs.energyfuels.5c06267 = DCBM-021

五、特殊元数据处理

Candidate 1：
- 与 DCBM-114 同为 XI Zhaodong、2026；
- DOI和题名不同则记录 same_author_year_different_paper。

Candidate 9：
- 不得编造 DOI；
- 查询期刊页、Crossref 和 DOI 注册源；
- DOI仍未确认时留空，按题名—作者—年份—卷期查重。

Candidate 10：
- DOI 在 2026 年注册，正式卷期日期为 2027-01-01；
- 同时记录 online metadata 与 formal issue year；
- 不得误标为预印本。

Candidates 11–13：
- manual_review_only；
- 核查实际埋深及知识库深部定义；
- 未通过人工相关性复核前不得入主表，也不得占用最终编号。

六、最终编号

- 所有日报编号均为 provisional；
- 读取执行时最后一个实际 DCBM ID；
- 仅对通过去重、元数据核验和纳入边界的候选连续编号；
- 重复和 manual_review_only 不占号；
- 不产生编号空洞；
- 不修改既有 ID。

七、正式写入

仅对正式非重复候选：
1. 更新 00_Master/Deep_CBM_Latest.xlsx；
2. 保留全部 sheet、格式、公式、超链接、批注和人工字段；
3. 新建 snapshot，不覆盖历史 snapshot；
4. 生成 increment Excel、RIS、BibTeX、DOI list；
5. 生成 duplicate check 和 update log；
6. 重新生成 JSONL/CSV master index；
7. 生成 Master_Index_Report 和 QC report；
8. 更新 CHANGELOG.md。

八、QC

确认：
- 工作簿可打开；
- 第一张 sheet 仍为完整文献矩阵；
- 8 个活动 sheet 完整；
- ID连续唯一；
- DOI/英文题名/中文题名重复数均为0；
- 主表、JSONL、CSV数量一致；
- increment Excel/RIS/BibTeX/DOI list 数量一致；
- skipped duplicate 含原因和 existing ID；
- manual_review_only 未误写入；
- Online First/未来卷期状态准确；
- CHANGELOG 与实际新增数一致；
- 保护目录未修改。

九、严禁修改

- 08_User/
- 00_Master/source/
- 00_Master/workbook_archive/
- 历史 snapshots
- 历史 increment
- 用户阅读标记、批注、自定义字段和人工排序

十、结果汇报

输出：
status
master_count_before
master_count_after
last_id_before
last_id_after
candidate_count
added_count
duplicate_skipped_count
manual_review_count
final_assigned_ids
duplicate_skipped_details
official_metadata_verified
online_first_statuses
DOI_duplicate_count
english_title_duplicate_count
chinese_title_duplicate_count
index_regenerated
qc_report_path
update_log_path
increment_directory
changelog_updated
protected_paths_modified
errors
warnings
```

# 11. Daily ingest manifest

```json
{
  "brief_date": "2026-07-23",
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
  "manual_review_count": 3,
  "known_duplicate_count": 5,
  "codex_action": "preflight_then_apply_verified_nonduplicates_only",
  "direct_repository_edit_performed": false,
  "protected_directory_edit_performed": false
}
```

# 12. 最终状态

```text
daily_brief_status: 10_recommended_candidates_plus_3_manual_review
repository_source_of_truth_checked: yes
master_record_count_at_check: 124
last_master_id_at_check: DCBM-124
recommended_add_count: 10
manual_review_count: 3
known_duplicate_count: 5
master_workbook_change_needed: pending_codex_live_deduplication
direct_repository_edit_performed: no
protected_directory_edit_performed: no
```
