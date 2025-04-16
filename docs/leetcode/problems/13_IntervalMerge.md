# 合并区间(Merge Intervals) - 学习笔记

## 题目概述
给定一个区间的集合，请合并所有重叠的区间。

## 关键点
1. Python数组排序
   - 使用 `.sort()` 方法进行原地排序
   - 使用 `.sorted()` 函数返回新的排序数组
   - 对于二维数组，需要使用 `key` 参数指定排序依据
   ```python
   # 原地排序
   intervals.sort(key=lambda x: x[0])
   
   # 返回新数组
   sorted_intervals = sorted(intervals, key=lambda x: x[0])
   ```

2. 区间合并的逻辑
   - 按照区间起点排序后，只需要比较相邻区间
   - 当前区间的起点小于等于前一个区间的终点时，需要合并
   - 合并时需要取两个区间终点的最大值
   ```python
   if res[-1][1] >= interval[0]:  # 需要合并
       res[-1][1] = max(res[-1][1], interval[1])
   ```

## 易错点
1. `.sort()` 和 `sorted()` 的区别
   - `.sort()` 是列表的方法，会修改原列表
   - `sorted()` 是内置函数，返回新的排序列表
   - 使用时要注意是否需要保留原列表

2. 合并区间时的终点选择
   - 错误示范：直接用新区间的终点
   ```python
   res[-1][1] = interval[1]  # 错误！
   ```
   - 正确做法：取两个终点的最大值
   ```python
   res[-1][1] = max(res[-1][1], interval[1])
   ```

## 完整代码
```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) <= 1:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    res = []
    
    for interval in intervals:
        if not res:
            res.append(interval)
        elif res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    
    return res
```

## 代码优化技巧
1. 空列表判断使用 `if not res` 而不是 `if res == []`
2. 对于二维数组的排序，使用 lambda 函数简化代码
3. 合并判断条件时注意逻辑的完整性

## 复杂度分析
- 时间复杂度：O(nlogn)，主要来自排序
- 空间复杂度：O(n)，需要存储结果数组

## 相关题目
1. 插入区间
2. 会议室
3. 区间列表的交集

## 总结
本题的核心在于：
1. 先对区间按起点排序
2. 排序后只需要关注相邻区间的关系
3. 合并时要取最大的终点值