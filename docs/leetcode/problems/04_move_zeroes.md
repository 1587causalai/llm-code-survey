# 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。


```python
## 1. 暴力解法

def moveZeroes(nums):
    zeros = [x for x in nums if x == 0]
    non_zeros = [x for x in nums if x != 0]
    return non_zeros + zeros

# test code
nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))

## 2. 双指针法
def moveZeroes(nums):
    n = len(nums)
    left = 0 # 第一个零元素指针
    right = 0 # 第一个非零元素指针
    while right < n:
        # 当右指针指向的元素不为0时，交换左右指针指向的元素
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left] # 交换之后, left 指针的元素不为零
            left += 1 # 更新左指针, i.e., 第一个零元素指针
        right += 1

# test code
nums = [0, 0, 1, 3, 12]
moveZeroes(nums)
print(nums)
```

可以考虑两个极端情况:
- 数组中没有0, left 和 right 始终都指向同一个元素
- 数组中全是0, left 永远不增加, 直到 right 遍历完数组

我们其实可以考虑一个**大局观的问题**, 要解决这个问题, 
- 只有一种操作, 那就是交换数值位置, 自然需要两个指针. 
- 交换的永远是: 零元素, 非零元素交换位置
- 自然是第一个个零元素, 和序列尾部第一个非零元素交换位置, 所以需要两个指针记录他们