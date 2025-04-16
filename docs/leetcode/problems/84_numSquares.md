# 完全平方数问题解析

## 题目描述
给定一个正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。求最少需要多少个完全平方数。

## 解法一：动态规划
这是最直观且易于理解的解法。

### 核心思路
- 定义 dp[i] 表示数字 i 最少需要多少个完全平方数来表示
- 对于每个数字 i，尝试用所有小于等于 i 的完全平方数来更新 dp[i]

### 代码实现
```python
def numSquares(self, n: int) -> int:
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 基础情况
    
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
            
    return dp[n]
```

### 时间复杂度分析
- 外层循环执行 n 次
- 内层循环对每个 i 执行 sqrt(i) 次
- 总时间复杂度为 O(n * sqrt(n))

## 解法二：数学方法
基于拉格朗日四平方和定理的解法。

### 核心思路
1. 任何正整数都可以表示为最多四个平方数之和
2. 通过数论知识可以进一步判断具体需要几个平方数

### 代码实现
```python
def numSquares(self, n: int) -> int:
    # 判断是否为完全平方数
    if int(sqrt(n)) ** 2 == n:
        return 1
    
    # 判断是否可以表示为两个平方数之和
    def isSum2(n):
        for i in range(1, int(sqrt(n)) + 1):
            j = int(sqrt(n - i * i))
            if i * i + j * j == n:
                return True
        return False
    
    # 判断是否需要四个平方数
    def isSum4(n):
        while n % 4 == 0:
            n //= 4
        return n % 8 == 7
    
    if isSum2(n):
        return 2
    if isSum4(n):
        return 4
    return 3
```

### 时间复杂度
O(sqrt(n))，主要消耗在判断是否为两个平方数之和的过程中。

## 解法三：记忆化搜索（完全背包思路）
这是一个不太直观但很巧妙的解法。

### 核心思路
- 将问题转化为完全背包问题
- 对于每个可用的完全平方数，决定是否使用它
- 使用记忆化搜索避免重复计算

### 代码实现
```python
@cache
def dfs(i: int, j: int):
    if i == 0:
        return float('inf') if j else 0
    if j < i * i:
        return dfs(i - 1, j)
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)

class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)
```

### 关键参数解释
- i：当前可以使用的最大完全平方数的根
- j：还需要凑成的目标数
- 返回值：凑成目标数所需的最少平方数数量

## 解法对比
1. 动态规划解法：
   - 优点：直观，容易理解和实现
   - 缺点：时间复杂度较高

2. 数学方法：
   - 优点：时间复杂度最低
   - 缺点：需要数论知识，不容易想到

3. 记忆化搜索：
   - 优点：空间复杂度较好，思路新颖
   - 缺点：代码不直观，难以理解和维护

## 实际应用建议
- 在面试中建议先说动态规划解法，因为最容易解释和理解
- 如果面试官继续追问，可以补充数学解法作为优化方案
- 记忆化搜索的解法虽然巧妙，但不建议作为首选方案，因为可读性较差