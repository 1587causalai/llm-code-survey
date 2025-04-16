# 二分查找插入位置的两种实现方法

## 问题描述
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

## 方法一：迭代实现
### 思路
使用双指针（left 和 right）不断缩小搜索范围，直到找到目标值或确定插入位置。

### 代码实现
```python
def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return left
```

### 关键点
1. 初始化左右指针，分别指向数组的起始和结束位置
2. 当左右指针相遇时结束循环
3. 每次比较中间元素与目标值：
   - 相等则返回中间索引
   - 大于目标值则在左半部分继续搜索
   - 小于目标值则在右半部分继续搜索
4. 最终 left 指针的位置就是应该插入的位置

## 方法二：递归实现
### 思路
通过递归调用不断缩小搜索范围，传递索引而不是创建新的子列表。

### 代码实现
```python
def searchInsert(self, nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left > right:
            return left
            
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)
    
    return binary_search(0, len(nums) - 1)
```

### 关键点
1. 使用辅助函数 binary_search 进行递归
2. 基本情况：当 left > right 时，返回 left 作为插入位置
3. 每次递归：
   - 计算中间位置
   - 根据比较结果在左半部分或右半部分继续搜索
4. 通过传递索引范围而不是创建新的子列表来优化空间复杂度

## 性能分析
两种方法的性能特征：
- 时间复杂度：O(log n)，每次将搜索范围缩小一半
- 空间复杂度：
  - 迭代方法：O(1)，只需要常数空间
  - 递归方法：O(log n)，需要递归调用栈的空间

## 使用建议
- 在一般情况下，推荐使用迭代方法，因为：
  1. 空间复杂度更低
  2. 不会有递归栈溢出的风险
  3. 代码更直观易懂
- 如果追求代码的简洁性或者在处理其他类似的递归问题时，递归方法也是一个不错的选择