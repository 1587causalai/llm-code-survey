# 零钱兑换问题解题笔记

## 问题描述
给定一个整数数组 coins，表示不同面额的硬币；以及一个整数 amount，表示总金额。计算凑成总金额所需的最少硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。可以认为每种硬币的数量是无限的。

## 初次尝试（存在问题的代码）
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount//coins[0]
            else:
                return -1

        if amount == 0:
            return 0

        last = max(coins)
        subset = [x for x in coins if x != last]

        res = []
        # 不用 last
        res.append(self.coinChange(subset, amount))

        # 使用 last
        j = 1
        while j * last <= amount:
            res.append(self.coinChange(subset, amount-j*last) + j)
            j += 1

        tmp = [x for x in res if x != -1]
        if tmp == []:
            return -1
        else:
            return min(tmp)
```

### 初始代码的问题分析
1. **边界条件处理问题**
   - 当coins长度为1时的边界条件虽然正确
   - 但在递归过程中，当subset递归到只剩一个硬币时，会重复触发这个边界条件
   - 返回的-1可能并不代表真正的"无解"，因为还有其他硬币可用

2. **递归逻辑的缺陷**
   - 每次取最大面额的做法，可能导致漏掉更优解
   - res数组收集所有可能结果，空间利用效率低
   - 不用last和用j个last的分支处理复杂且容易出错

3. **易错点标注**
   ```python
   # 这里的边界条件判断顺序有问题
   if len(coins) == 1:  # 应该先判断amount == 0
       if amount % coins[0] == 0:
           return amount//coins[0]
       else:
           return -1

   # 这里的-1过滤可能过滤掉有效解
   tmp = [x for x in res if x != -1]  # 需要更细致地判断子问题的结果
   ```

## 改进尝试
尝试修复边界条件：
```python
def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
        
    if amount < 0 or not coins:
        return -1
        
    last = max(coins)
    subset = [x for x in coins if x != last]
    
    min_coins = float('inf')  # 改用float('inf')标记未找到解
    j = 0
    while j * last <= amount:
        sub_result = self.coinChange(subset, amount - j * last)
        if sub_result != -1:
            min_coins = min(min_coins, sub_result + j)
        j += 1
        
    return min_coins if min_coins != float('inf') else -1
```

## 最终动态规划解决方案
```python
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

## 关键洞察

### 1. float('inf') 的巧妙运用
这是解题过程中最精妙的设计：
- 使用 float('inf') 而不是 -1 来标记"无法到达"的状态
- 在 min() 运算中能自然维护这个状态
- dp[x - coin] + 1 运算也能保持正确性
- 最后只需简单判断是否仍为 float('inf')

### 2. 动态规划的状态定义
- dp[i] 表示凑出金额 i 最少需要的硬币数
- dp[0] = 0 表示凑出金额0不需要硬币
- 其他位置初始化为无穷大，表示还未找到方案

### 3. 转移方程的简洁性
对于每个金额x和硬币coin：
- 如果用这个硬币：dp[x - coin] + 1
- 如果不用这个硬币：保持原值 dp[x]
- 取两者最小值

## 经验总结

1. **不要被题目表述限制思维**
   - 题目说返回-1表示无解
   - 但在实现时使用 float('inf') 可能是更好的选择

2. **警惕复杂的边界条件**
   - 如果发现边界条件处理过于复杂，很可能是解法不够优雅
   - 边界条件多容易顾此失彼，应该寻找能统一处理的方案

3. **递归到动态规划的转化**
   - 递归解法直观但可能有重复计算
   - 复杂的递归边界条件往往暗示可以用动态规划优化

## 扩展思考
- 如果硬币数量有限制，如何修改解法？
- 如果需要输出具体的硬币组合，如何修改解法？
- 在实际工程中，是否需要考虑大数问题？