# 单调栈解题思路与信息存储选择的深度思考

## 1. 问题引入：每日温度问题

给定一个数组 `temperatures`，要求计算对于每一天，需要等待多少天才能遇到一个更高的温度。如果未来不存在更高的温度，则存储0。

## 2. 初始思路的困境

最初的解法尝试在栈中存储温度值：

```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0 for _ in temperatures]
    n = len(temperatures)
    stack = [temperatures[0]]  # 存储温度值
    i = 0
    while i <= n-2 and stack:
        i = i + 1
        j = 0
        while stack and temperatures[i] > stack[-1]:
            res[i-j-1] = 1+j
            j += 1
            stack.pop()
        stack.append(temperatures[i])
    return res
```

这个解法存在的问题：
1. 需要额外的计数器j来计算距离
2. 索引计算复杂且不直观 (`i-j-1`)
3. 循环结构复杂

## 3. 优化解法：存储索引的重要性

改进后的解法选择存储索引而不是温度值：

```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    res = [0] * n
    stack = []  # 存储索引
    
    for curr_idx in range(n):
        curr_temp = temperatures[curr_idx]
        
        while stack and curr_temp > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            res[prev_idx] = curr_idx - prev_idx
            
        stack.append(curr_idx)
    
    return res
```

优势：
1. 状态追踪清晰
2. 距离计算直观 (`curr_idx - prev_idx`)
3. 代码结构简单

## 4. 思维定势分析

为什么我们容易陷入存储温度值的思维定势？

1. **直觉陷阱**
   - 题目描述关注"找更高温度"，容易让我们关注温度值
   - 比较大小的本能反应是存储要比较的值

2. **问题转化意识**
   - 题目本质是"计算距离"而不是"找更大值"
   - 需要从表面描述跳转到本质需求

## 5. 启发式方法

解决此类问题的三步法：

1. **模式识别**
   - 识别"找下一个更XXX的元素"模式
   - 联想到单调栈的适用场景

2. **信息选择**
   - 问自己"最终要计算什么？"
   - 计算距离→存索引
   - 计算值的差→存值

3. **验证思路**
   - 用简单例子验证选择的合理性

## 6. 变种问题的启示

如果改变问题为求温差而不是天数差：

```python
def temperatureDifference(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    res = [0] * n
    stack = []  # 需要同时存储温度和索引
    
    for i in range(n):
        curr_temp = temperatures[i]
        
        while stack and curr_temp > stack[-1][0]:
            prev_temp, prev_idx = stack.pop()
            res[prev_idx] = curr_temp - prev_temp
            
        stack.append((curr_temp, i))
    
    return res
```

这个变种揭示：
1. 有时需要存储多个信息（温度值和索引）
2. 存储信息的选择不是非黑即白
3. 要根据计算需求来选择存储的信息

## 7. 关键启示

1. 识别问题的本质比表面描述更重要
2. 存储的信息应该直接服务于最终的计算需求
3. 代码复杂性常常来自信息表达方式的选择不当
4. 有时候需要多种信息的组合才能最优解决问题

## 8. 扩展思考

这种思维方式可以应用到更多场景：
- 当代码变得复杂时，考虑是否选择了最适合的信息表达方式
- 是否可以通过改变存储的信息来简化计算逻辑
- 是否需要存储多个维度的信息来满足计算需求