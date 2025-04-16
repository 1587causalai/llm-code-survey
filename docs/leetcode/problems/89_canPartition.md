# 分割等和子集问题解题思路

## 问题描述
给定一个**只包含正整数**的**非空**数组 nums，判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

## 关键思路突破
1. **问题转化是关键**
   - 原问题：将数组分成和相等的两个子集
   - 转化后：找到一些数，使它们的和等于整个数组和的一半(sum/2)
   - 转化的合理性：如果找到和为sum/2的一组数，剩下的数之和必然也是sum/2

2. **为什么这个转化很重要？**
   - 简化了问题：从"分成两个子集"变成"找一个子集"
   - 明确了目标：给了一个具体的目标值sum/2
   - 让我们能够更容易地定义dp数组

## 动态规划解法

### DP数组定义
- dp[i][j]表示：使用前i个数字，能否恰好凑出和为j的子集
- i：考虑的数字范围（前i个数字）
- j：目标和（当前需要凑出的和）

### 状态转移
对于第i个数字nums[i-1]，有两种选择：
1. 不选：dp[i][j] = dp[i-1][j]
2. 选：dp[i][j] = dp[i-1][j-nums[i-1]]  (如果j >= nums[i-1])

最终状态转移方程：
```python
if j < nums[i-1]:
    dp[i][j] = dp[i-1][j]
else:
    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
```

## 完整代码
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:  # 总和为奇数，必然不可能平分
        return False
    target = total // 2
    
    # dp[i][j] 表示能否用前i个数凑出和为j
    dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
    dp[0][0] = True  # 空集的和为0
    
    for i in range(1, len(nums) + 1):
        for j in range(target + 1):
            if j < nums[i-1]:  # 当前数字太大，不能选
                dp[i][j] = dp[i-1][j]
            else:  # 可以选择当前数字或不选
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    return dp[len(nums)][target]
```

## 解题启示
1. **问题转化的重要性**
   - 好的转化能够让问题变得更清晰
   - 转化后更容易想到使用什么算法
   - 转化是找到dp数组定义的关键

2. **与其他问题的联系**
   - 本质上是0-1背包问题的变体
   - 背包容量是sum/2
   - 物品重量就是数组中的数字
   - 目标是恰好装满背包

3. **思维方法总结**
   - 遇到复杂问题时，先尝试转化简化
   - 看能否转化成熟悉的问题模型（如背包问题）
   - 通过转化来帮助定义dp数组

## 与三数之和问题的对比

### 问题特点对比
1. **问题类型**
   - 分割等和子集：判定性问题（返回true/false）
   - 三数之和：求解所有可能的组合（返回具体解）

2. **解法选择**
   - 分割等和子集：适合用动态规划
     * 需要考虑所有可能的选择组合
     * 有重叠子问题
     * 求解的是"是否存在"的问题
   - 三数之和：适合用双指针
     * 可以通过排序优化搜索空间
     * 需要找出所有具体的组合
     * 利用排序后数组的有序性质

3. **算法思维区别**
   - 分割等和子集：
     * 思维重点在于问题转化
     * 转化为背包问题后使用dp
     * 核心是"选或不选"的思维模式
   - 三数之和：
     * 思维重点在于搜索优化
     * 通过排序+双指针降低时间复杂度
     * 核心是"收缩区间"的思维模式

### 三数之和代码示例
```python
def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:  # 跳过重复元素
            continue
            
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                # 跳过重复元素
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

## 相关问题
- 0-1背包问题
- 目标和问题（给数组中的每个数添加+/-号，求目标和的方案数）
- 三数之和为0问题（虽然解法不同，但都需要思考如何简化问题）