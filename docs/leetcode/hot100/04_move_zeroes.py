"""
移动零

给定一个数组 nums，将所有零移动到数组的末尾，同时保持非零元素的相对顺序。
"""
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
    left = 0
    right = 0
    while right < n:
        # 当右指针指向的元素不为0时，交换左右指针指向的元素
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left] # 交换之后, left 指针的元素不为零
            left += 1 # 更新左指针
        right += 1

# test code
nums = [0, 0, 1, 3, 12]
moveZeroes(nums)
print(nums)