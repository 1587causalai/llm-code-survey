# 字符串划分问题解题笔记

## 题目描述
给定一个字符串 `s`，要求将其划分为尽可能多的片段，同时要求同一个字母最多只能出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

## 解题思路演进

### 初始误解
最初误解了题目要求，以为是"同一个片段中不能出现相同的字母"。基于这个误解写出了错误的代码：

```python
def partitionLabels(self, s: str) -> List[int]:
    if s == '':
        return []

    curr = []
    res = []
    for char in s:
        if char in curr:
            res.append(len(curr))
            curr = [char]
        else:
            curr.append(char)

    res.append(len(curr))
    return res
```

这个解法的问题在于：它只是在遇到重复字母时就切分字符串，没有考虑到字母在后面还可能出现的情况。

### 区间合并思路
理解题目后，想到可以将问题转化为区间合并问题：
1. 记录每个字母首次和最后一次出现的位置，形成区间
2. 将重叠的区间合并
3. 计算每个合并后区间的长度

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s == '':
            return []

        # 记录每个字母的区间
        intervals = {}
        for i, char in enumerate(s):
            if char not in intervals:
                intervals[char] = [i, i]
            else:
                intervals[char][1] = i
        
        # 将区间列表排序
        interval_list = sorted(intervals.values())
        
        # 合并重叠区间
        merged = []
        for interval in interval_list:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        # 计算每个区间的长度
        return [end - start + 1 for start, end in merged]
```

### 优化解法
进一步思考发现，我们其实不需要真正地构建和合并区间，只需要：
1. 记录每个字母最后出现的位置
2. 遍历字符串时维护当前片段的结束位置
3. 当遍历到结束位置时，就完成一个片段的划分

```python
def partitionLabels(self, s: str) -> List[int]:
    # 记录每个字母最后出现的位置
    last_pos = {}
    for i, char in enumerate(s):
        last_pos[char] = i
    
    result = []
    start = 0
    end = 0
    
    # 遍历字符串
    for i, char in enumerate(s):
        # 更新当前片段的结束位置
        end = max(end, last_pos[char])
        
        # 如果到达片段结束位置，记录片段长度
        if i == end:
            result.append(end - start + 1)
            start = i + 1
            
    return result
```

## 解法比较
1. **区间合并解法**：
   - 优点：思路直观，易于理解
   - 缺点：需要额外空间存储区间，时间复杂度较高(O(nlogn))
   - 适用场景：当问题可以明显转化为区间合并问题时

2. **优化解法**：
   - 优点：时间复杂度更低(O(n))，空间利用更高效
   - 缺点：思路不如区间合并直观
   - 适用场景：实际应用中推荐使用这种解法

## 学习心得
1. 仔细理解题目要求很重要，最初的误解导致解题方向完全错误
2. 问题可以有多种解决思路，要学会从不同角度思考
3. 在找到可行解后，思考是否有优化空间
4. 通过对比不同解法，加深对问题的理解

## 相关题目
- 合并区间
- 会议室问题
- 其他区间相关问题

## 总结
这道题是一个很好的例子，展示了如何从错误理解到逐步优化的解题过程。通过不断讨论和思考，最终得到了一个优雅的解决方案。这个过程也强调了理解题意和持续优化的重要性。