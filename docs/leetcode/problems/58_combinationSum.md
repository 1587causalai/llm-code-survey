# 回溯算法理解笔记

## 1. 什么是回溯算法？
回溯算法可以理解为"聪明的穷举"。它通过系统性的尝试，在发现某个选择不可行时及时停止并回退，换其他选择继续尝试。

### 1.1 核心思想
- 一步一步尝试可能的解
- 发现走不通时及时停止
- 回退到上一步
- 尝试其他可能的选择

## 2. 最简单的例子：凑零钱问题
假设我们只有面值为2元和5元的硬币，要凑出7元，可以用回溯算法找出所有可能的组合。

### 2.1 代码实现
```python
def coin_combinations(coins, target):
    result = []  # 存储所有可行的组合
    current = []  # 当前正在尝试的组合
    
    def try_combination(remaining):
        # 找到一个解
        if remaining == 0:
            result.append(current[:])
            return
            
        # 明显不可能的情况
        if remaining < 0:
            return
            
        # 尝试每个硬币
        for coin in coins:
            current.append(coin)  # 选择这个硬币
            try_combination(remaining - coin)  # 继续尝试凑剩下的钱
            current.pop()  # 不要这个硬币，尝试下一个
    
    try_combination(target)
    return result
```

### 2.2 执行过程详解
假设输入：coins = [2, 5], target = 7

执行过程是这样的：
```
当前组合[], 还需要凑7
└── 选择2:
    当前组合[2], 还需要凑5
    └── 选择2:
        当前组合[2,2], 还需要凑3
        └── 选择2: [2,2,2] 需要凑1，不行，回退
        └── 选择5: [2,2,5] 需要凑-2，不行，回退
    └── 选择5:
        当前组合[2,5], 还需要凑0，找到一个解！
└── 选择5:
    当前组合[5], 还需要凑2
    └── 选择2: [5,2] 找到另一个解！
    └── 选择5: [5,5] 超过了，不行
```

### 2.3 关键点解释
1. **为什么不会卡在第一个选择？**
   - for循环会遍历所有可能的选择
   - 每层的for循环都维护着自己的进度
   - return后会继续for循环中未完成的部分

2. **return 的作用**
   - 不带返回值的return表示"这条路试过了，回去试另一条路"
   - 回到上一层的for循环继续尝试未试过的选择

3. **current.pop() 的作用**
   - 在尝试完一个选择后撤销这个选择
   - 为尝试下一个选择做准备
   - 保证current数组始终反映当前的选择路径

## 3. 回溯算法的一般模式
```python
def backtrack(路径, 选择列表):
    if 满足结束条件:
        保存结果
        return
        
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```

## 4. 理解难点和建议
### 4.1 主要难点
1. 递归思维的难度
   - 一层调一层
   - 每层都有自己的状态
   - 需要理解"回退"过程

2. 状态管理的复杂性
   - 什么时候加入结果
   - 什么时候回退
   - 如何避免重复

### 4.2 学习建议
1. 从简单例子开始
2. 画图帮助理解
3. 添加打印语句跟踪执行过程
4. 先掌握基本模式，再解决复杂问题

## 5. 思考题
[LeetCode题目：组合总和](https://leetcode.com/problems/combination-sum/)
```python
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []
    
    def backtrack(remain: int, curr: List[int], start: int):
        if remain == 0:
            result.append(curr[:])
            return
            
        if remain < 0:
            return
            
        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            backtrack(remain - candidates[i], curr, i)
            curr.pop()
    
    backtrack(target, [], 0)
    return result
```
这个问题可以在掌握基础概念后再来理解和解决。