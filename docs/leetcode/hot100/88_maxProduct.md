# 动态规划解题笔记: 乘积最大子数组

## 问题描述
给你一个整数数组 `nums`，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

## 核心难点
这个问题乍看是一个简单的动态规划问题，但实际上有一个重要的难点：数组中可能包含负数。这导致了一个有趣的现象：

1. 当遇到正数时，我们希望之前的乘积越大越好
2. 当遇到负数时，我们希望之前的乘积越小越好（因为负数乘以负数会变成正数）

这就导致了传统的动态规划方法（只记录最大值）无法正确处理所有情况。

## 错误示范
一个容易想到但存在问题的解法：

```python
def maxProduct(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [float('-inf') for x in nums]  # dp[i]表示以nums[i]结尾的最大乘积
    dp[0] = nums[0]

    for i in range(1, n):
        if nums[i] > 0:
            dp[i] = max(nums[i], nums[i] * dp[i-1])
    # ...这个解法无法正确处理负数情况
```

这个解法的问题在于：
1. 只考虑了正数的情况
2. 没有记录最小值，导致无法处理负数情况

## 正确解法
### 核心思路
1. 维护两个dp数组：
   - dpMax[i]: 表示以nums[i]结尾的子数组的最大乘积
   - dpMin[i]: 表示以nums[i]结尾的子数组的最小乘积

2. 对于每个位置i，最大值可能来自：
   - nums[i]本身（重新开始一个子数组）
   - dpMax[i-1] * nums[i]（当nums[i]为正数时）
   - dpMin[i-1] * nums[i]（当nums[i]为负数时）

### 代码实现（数组版）
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dpMax = [0 for _ in range(n)]
        dpMin = [0 for _ in range(n)]
        
        # 初始化
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        result = nums[0]
        
        for i in range(1, n):
            dpMax[i] = max(nums[i], 
                          nums[i] * dpMax[i-1], 
                          nums[i] * dpMin[i-1])
            dpMin[i] = min(nums[i], 
                          nums[i] * dpMax[i-1], 
                          nums[i] * dpMin[i-1])
            
            result = max(result, dpMax[i])
            
        return result
```

### 空间优化版本
由于我们每次只需要前一个位置的结果，可以将空间复杂度从O(n)优化到O(1)：

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        curMax = nums[0]  # 当前位置的最大乘积
        curMin = nums[0]  # 当前位置的最小乘积
        result = nums[0]
        
        for i in range(1, n):
            # 注意要使用临时变量
            tmpMax = max(nums[i], nums[i] * curMax, nums[i] * curMin)
            tmpMin = min(nums[i], nums[i] * curMax, nums[i] * curMin)
            
            curMax = tmpMax
            curMin = tmpMin
            result = max(result, curMax)
            
        return result
```

## 复杂度分析
- 时间复杂度：O(n)，其中n是数组长度
- 空间复杂度：
  - 数组版本：O(n)
  - 优化版本：O(1)

## 关键点总结
1. 理解为什么需要同时维护最大值和最小值
2. 每次计算都要考虑从当前位置重新开始的可能性
3. 在使用变量而非数组时，注意要用临时变量避免相互影响
4. 这是一个典型的需要考虑负数特殊情况的动态规划问题

## 相关题目
- 最大子数组和（53. Maximum Subarray）
- 乘积为正数的最长子数组（1567. Maximum Length of Subarray With Positive Product）

希望这个笔记能帮助理解这个有趣的动态规划问题！