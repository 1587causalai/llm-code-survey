# 多数元素

## 题目描述

给定一个大小为 n 的数组 nums，返回其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

## 解法分析

这道题有多种解法，我们从简单到复杂逐一分析：

### 解法一：哈希表计数

最直观的解法是使用哈希表统计每个元素出现的次数。

```python
def majorityElement(nums):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
        if counter[num] > len(nums) // 2:
            return num
```

- 时间复杂度：O(n)
- 空间复杂度：O(n)
- 优点：直观易懂
- 缺点：需要额外的存储空间

### 解法二：排序法

由于多数元素出现次数超过 n/2，排序后中间的元素必定是多数元素。

```python
def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]
```

- 时间复杂度：O(n log n)
- 空间复杂度：O(1) 或 O(n)（取决于排序算法的实现）
- 优点：实现简单
- 缺点：需要修改输入数组或使用额外空间

### 解法三：Boyer-Moore 投票算法（最优解）

这是一个非常巧妙的算法，可以在 O(n) 时间和 O(1) 空间内解决问题。

```python
def majorityElement(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
            
    return candidate
```

- 时间复杂度：O(n)
- 空间复杂度：O(1)
- 优点：时空复杂度最优，实现简单
- 缺点：需要理解算法原理

## Boyer-Moore 算法原理解释

这个算法可以类比为一个特殊的拳击比赛场景，这样更容易理解：

想象一个不太寻常的拳击比赛：
1. 有一个最厉害的拳击手（就是我们要找的多数元素），他的支持者超过了总人数的一半
2. 比赛规则很特别：
   - 每次只能两个人上场对打
   - 每场比赛后，两个人都要离场（不管输赢）
   - 如果场上只剩一个人，他就继续留着等下一个对手
3. 比赛过程：
   - 如果两个不同派系的人打架，就互相消耗掉了
   - 如果两个同派系的人，其中一个可以"转移能量"给另一个，然后离场

因为厉害拳击手的支持者超过一半，即使其他所有派系都联合起来，最后场上留下的，一定是那个厉害拳击手的支持者！

这就是 Boyer-Moore 算法的本质，可以类比为一个特殊的"能量对抗"过程：

1. **初始状态**：
   - count = 0（能量值）
   - candidate = None（当前候选者）

2. **对抗规则**：
   - 当能量值为0时，选择当前元素作为新的候选者
   - 遇到相同元素，能量值+1
   - 遇到不同元素，能量值-1

3. **正确性证明**：
   - 由于多数元素出现次数 > n/2
   - 即使其他所有元素都联合起来对抗它
   - 最后留下的必定是多数元素

### 示例演示

以数组 [2,2,1,1,2] 为例：

```
初始：count=0, candidate=None
遇到2：count=1, candidate=2
遇到2：count=2, candidate=2
遇到1：count=1, candidate=2
遇到1：count=0, candidate=2
遇到2：count=1, candidate=2
最终结果：2
```

## 代码实现要点

1. **变量说明**：
   - count：记录当前候选者的"能量值"
   - candidate：当前的候选者

2. **关键步骤**：
   - 检查能量值是否为0（count == 0）
   - 更新能量值（count += 1 或 -1）
   - 返回最终的候选者

3. **边界处理**：
   - 由于题目保证存在多数元素，不需要特别的边界处理
   - 算法总能找到正确答案

## 复杂度分析

- **时间复杂度**：O(n)
  - 只需要遍历一次数组
  - 每个元素的处理时间是常数级

- **空间复杂度**：O(1)
  - 只使用了两个变量（count和candidate）
  - 不需要额外的数据结构

## 总结

Boyer-Moore 投票算法是解决多数元素问题的最优解，它巧妙地利用了多数元素出现次数超过 n/2 这个特性，通过"能量对抗"的方式找到答案。虽然算法看起来有点技巧性，但背后的思想还是很符合直觉的。在面试中，理解和运用这个算法不仅能展示编程能力，还能体现对算法设计的深入理解。