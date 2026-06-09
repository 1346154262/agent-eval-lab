# Agent Eval Lab

[English](README.md) | 简体中文

Agent Eval Lab 是一个面向业务 Agent 的 Harness 式评测实验仓库。它的核心思想是：用 Codex、ClaudeCode 这类强 Agent 作为 Harness Builder，帮助你设计评测方案、构建黄金评测集、编写评测 Agent Prompt、汇总结果并提出改进建议。

这个仓库希望把变化快、业务相关的评测逻辑，从零散 Python 脚本中抽出来，沉淀为 Prompt、Rubric、Schema、模板和可复用资产。Python 脚本只负责确定性的部分，例如数据集校验和结果汇总。

## 仓库包含什么

- 一个 Codex 兼容的 Agent 评测 Skill。
- Harness 式评测方法说明。
- L1/L2/L3 三层指标体系。
- 评测方案、评测 Agent Prompt、Judge Rubric、Dataset、Result、Error Taxonomy 模板。
- 一个分类 Agent 的最小示例。
- 轻量脚本：数据集校验和结果汇总。

## 核心方法

传统评测常见问题是启动成本高、迭代慢、指标分散、复现困难。Agent Eval Lab 采用 Harness 式评测：

1. 强 Agent 负责搭建评测骨架。
2. 人负责 GT 标注、方案审核、抽检和最终决策。
3. 评测逻辑尽量 Prompt 化，便于快速修改和复用。
4. 数据集保持小而精，优先覆盖边界和高风险场景。
5. 结果保留证据、错误分类和可复现输入。

## 三层指标体系

L1 是所有 Agent 必须具备的基础指标：

- 输出是否可解析
- 输出格式是否合规
- 必填字段是否完整
- 工具调用或最终答案是否存在

L2 是按能力类型选择的指标：

- 分类准确率
- 精确率和召回率
- 抽取精确匹配或部分匹配
- 数值抽取误差
- 检索覆盖率
- 指令遵循通过率

L3 是业务专属指标：

- 违禁词清洁率
- 品牌或语气一致性
- 业务规则命中率
- 领域安全规则
- 特定 Agent 工作流完成标准

## 快速开始

安装依赖：

```bash
python -m pip install -e ".[dev]"
```

校验示例数据集：

```bash
python agent-eval-lab/scripts/validate_dataset.py agent-eval-lab/examples/classification-agent/dataset.yaml
```

汇总示例评测结果：

```bash
python agent-eval-lab/scripts/summarize_results.py agent-eval-lab/examples/classification-agent/results.yaml --markdown report.generated.md --json report.generated.json
```

## 推荐工作流

1. 明确被测 Agent、业务任务、输出契约和上线风险。
2. 先写评测方案，不急着写 runner 代码。
3. 构建 20 到 55 条小而精的黄金评测集。
4. 选择 L1、L2、L3 指标。
5. 编写 Evaluator Agent Prompt。
6. 执行或指导评测。
7. 汇总失败类型、证据和改进建议。
8. 对高风险、边界或 Judge 敏感样本做人工抽检。

## 第一版边界

当前版本不直接调用 OpenAI、Anthropic、Claude 或其他模型 API。它更适合任务包评测、人工或半自动评分、报告生成和 Prompt 迭代验证。后续可以在不改变核心目录结构的前提下增加 API Runner。

## 适用场景

- Prompt 天级迭代验证。
- 多 Agent 横向对比。
- 新业务 Agent 上线验收。
- 把一次性评测经验沉淀成可复用模板。

## 不适用场景

- 需要大规模自动化 Benchmark 平台。
- 需要立即接入多个模型供应商并自动调用 API。
- 希望完全依赖 LLM-as-Judge 而不做人工抽检。

## License

MIT
