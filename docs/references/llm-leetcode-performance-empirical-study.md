# LLM代码生成性能分析：基于LeetCode的实证研究

> Coignion T, Quinton C, Rouvoy R. A Performance Study of LLM-Generated Code on Leetcode[C]//Proceedings of the 28th International Conference on Evaluation and Assessment in Software Engineering. 2024: 79-89.


## 研究背景与意义

随着Large Language Models (LLMs)在代码生成领域的广泛应用，对其生成代码的性能评估变得尤为重要。与以往主要关注代码正确性和安全性的研究不同，本研究首次系统性地评估了LLM生成代码的运行时性能特征。这一研究方向对于理解AI辅助编程的实际效能具有重要意义。

## 研究方法

### 实验设计
- **数据集构建**：
  - 精选204个LeetCode问题(56简单, 104中等, 44困难)
  - 选取2023年1月后发布的题目以规避数据污染
  - 确保每个问题具有可测量的性能差异性(O(n)到O(n²)的算法复杂度跨度)

- **模型选择**：
  - 评估18个代码生成LLM，包括：
    - GitHub Copilot (11B参数)
    - CodeLlama系列 (7B-13B参数)
    - StarCoder (15.5B参数)
    - 其他主流开源模型
  - 统一使用Python作为目标语言

### 性能评估框架
1. **代码生成流程**：
   - 每个问题生成10个解决方案
   - temperature参数范围：0.1-1.0（6个等级）
   - GitHub Copilot使用默认temperature

2. **验证流程**：
   - 本地语法验证
   - LeetCode在线评判系统验证
   - 性能基准测试（排除运行时间>10s的解决方案）

3. **性能度量指标**：
   - Pass@k指标评估功能正确性
   - 使用pytest-benchmark测量运行时间
   - LeetCode排名评估相对性能
   - Cohen's d效应量评估模型间差异

### 统计分析方法

#### 1. 模型间性能差异检验
配对t检验统计量：

$$
t = \frac{\bar{d}}{s_d/\sqrt{n}}
$$

其中：
- $\bar{d}$ 为差值的平均数
- $s_d$ 为差值的标准差
- n 为样本量

#### 2. Temperature影响分析
Pearson相关系数计算：

$$
r = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}}
$$

其中：
- $(x_i, y_i)$ 为配对观测值
- $(\bar{x}, \bar{y})$ 为各自的平均值

## 核心发现

1. **模型性能差异分析**
   - 模型间性能差异的Cohen's d效应量仅为0.024
   - StarCoder和CodeLlama-13B-python展现出略微优势
   - 模型规模与代码性能无显著相关性

2. **生成代码与人类对比**
   - LLM生成的有效解决方案平均超过73%的人类提交
   - 在部分问题上达到了95%以上的性能水平

3. **Temperature影响**
   - Temperature与代码性能无显著相关(相关系数0.05)
   - Temperature与性能变异性呈中等正相关(0.41)
   - 较高temperature有助于探索更多样的解决方案

4. **功能正确性与性能关系**
   - 成功率与运行时间呈弱负相关(-0.08)
   - 模型准确性与代码性能无显著关联

## 研究局限性

1. **数据集限制**：
   - 仅限于算法问题，可能不完全代表实际应用场景
   - LeetCode平台的测量稳定性存在一定波动

2. **性能评估局限**：
   - 未考虑内存使用等其他性能指标
   - 测试用例规模可能影响性能排序

## 研究启示

1. **模型选择**：
   - 在代码性能方面，较小的模型可能已经足够
   - 模型规模不应作为性能优化的主要考虑因素

2. **实践建议**：
   - 可以通过调整temperature来获得更多样的解决方案
   - LLM生成的代码在性能上具有竞争力

## 未来研究方向

1. 开发性能导向的训练数据集
2. 探索针对性能优化的模型微调方法
3. 扩展到更广泛的编程任务场景

