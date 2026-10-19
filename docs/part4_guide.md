# Part 4 最终交接说明

负责人：HUANG Ze（1155280222）。本交付是模块 4，不是替全组完成或提交最终总报告。

## 交付范围

1. P5 推导、二维有效谱/条件数、稳定区间、eta=1 的 minimax 步长。
2. 沿用公共 preconditioning.py / runner.py，不修改其他成员的算法定义；新增独立 P5 实验和测试。
3. 对历史正式输出的 10,200 个评估 run、6,600 对进行只读核对。
4. 首次达到和最终保留两种四格成功表、独立 run 的分母统计、失败计数、固定预算 log-gap、配对效应、达到时间比。
5. 二维联合 initial-ID / 高维 rotation-cluster bootstrap，2,000 次，固定 seed，描述性点态 95% 区间。
6. 条件数/收敛图、二维 gap maps、角度效应图、高维区间图、成功表/保留图及失败图。
7. 英文模块报告 PDF/LaTeX、中文说明、可运行源码、测试、原始结果与来源哈希。

## 不可省略的限制

- 正式数据是 commit 575ebf4 的历史结果；整合源码是 bb365b9。统计是对保存结果的分析，不是把当前源码当成历史执行源码。
- 本轮 verifier 全部结构核验通过；每阶段 10 个、共 30 个数值复跑中，2 个 eigenbasis-Adam run 的 9 个字段超出容差，因此 numerical_checks_passed=false。原始 verification.json 的旧 passed 标记没有被覆盖。
- 整合包另有前次 450 样本中 56 个 run 失配的记录，与本轮 30 个样本分开说明。
- 所有运行都曾达到 1e-6，不代表最后成功。Adam 的 transfer 保留 777/850，retune 795/850；总计 1572/1700。
- late-stage Adam/eigenbasis Adam 不一致不能直接推翻精确算术理论；retune 还可能改变两边学习率。
- 未声称完成独立、受控的 setup-inclusive 成本基准。零 setup_seconds 不能当作无预条件成本。该计时是 Proposal 次要扩展，报告中明确限制。
- bootstrap 只有每格 10 个独立方向/旋转，区间不是同时置信带，也没有包括跨平台不确定性；全成功的退化区间不是成功概率为 1 的证明。

## 复现（无需重新跑主实验）

在 project/ 目录，安装已有项目依赖及 matplotlib：

```bash
python -m pip install -e '.[plots]'
python scripts/reproduce_part4.py
```

重建 PDF 需要 TeX Live/MiKTeX/MacTeX 的 pdflatex：

```bash
python scripts/reproduce_part4.py --report
```

已有 PDF 可直接阅读，没有 LaTeX 也能重做所有 CSV 和图。
复现脚本会重建 Part 4 输出，但不会改写 outputs/part3/ 历史数据。
审计 JSON 中保留实际生成环境版本；参考环境锁定在 requirements-part4.txt。
所有既有 89 项测试和新增的 Part 4 测试须通过。测试通过不替代主实验的数值复现。

## 给整合同学的合并顺序

1. 先核对仓库基线，当前目标是 bb365b9；不要直接用历史 part3-v1 覆盖 main。
2. 将 part4_merge/ 中同路径新增文件复制到仓库。没有修改公共算法文件。
3. 大型历史 outputs/part3/ 不必推到 Git；最终完整包已经包含它们。Release 可以附完整包，仓库只放模块源码/测试/文档。
4. 执行 Part 4 测试及复现命令，对照 summary CSV 和报告数字。
5. 在总报告加入 P5、统计方法、成功/保留区分、效应与 bootstrap，选择少量图，并保留数值复现限制。
6. 另一位同学独立复查公式、配对结构和关键表；独立复查尚需组员完成，不能把本轮程序测试写成他人复现。
7. 报告/代码使用了 AI 辅助整理与实现，请按课程 AI 使用规范检查、理解并披露，不要未经阅读直接以个人独立完成名义提交。

## 重要路径

- outputs/part4/part4_report.pdf：英文模块报告。
- outputs/part4/stats/：逐对数据、汇总、成功表、失败表、审计。
- outputs/part4/figures/：正式历史统计图；outputs/part4/*.png 是独立 P5 图。
- outputs/part4/audit/：本轮只读 verifier、单元测试日志、输入来源核对。
- docs/part4_report.tex：报告正文；part4_generated_tables.tex 为真实 CSV 生成的表。
- docs/part4_checkpoint.md 和 part4_plan_zh.md 是第一阶段历史记录；以本说明为当前状态。
