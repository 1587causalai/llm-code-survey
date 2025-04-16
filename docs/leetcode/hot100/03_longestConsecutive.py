"""
给定一个未排序的整数数组 nums，找到数字连续区间的最长长度。

e.g. 给定 [100, 4, 200, 1, 3, 2], 返回 4
"""
# 1. 暴力解法
def longestConsecutive(nums):
    # 1. 先排序
    nums.sort()

    # 2. 遍历
    max_len = 0
    cur_len = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            cur_len += 1
        elif nums[i] == nums[i-1]:
            continue
        else:
            max_len = max(max_len, cur_len)
            cur_len = 1

    # for e.g. [1,2,3,4,4,5]
    max_len = max(max_len, cur_len)
    return  max_len

# test case
nums = [100, 4, 200, 1, 3, 2, 2]
print('test case for brute force:')
print(longestConsecutive(nums))  # 4

# 2. 哈希表

def longestConsecutive(nums):
    # 1. 先去重
    nums = list(set(nums))

    # 2. 哈希表
    hash_map = {}
    for num in nums:
        hash_map[num] = 1 # 表示这个数字出现过, 有去掉重复的作用

    # 3. 遍历
    max_len = 0
    for num in hash_map:
        # 如果num-1不在哈希表中，说明是一个连续序列的开始
        if num - 1 not in hash_map:
            cur_len = 1
            cur_num = num
            # 一直往后找 cur + 1，直到找不到为止
            while cur_num + 1 in hash_map: 
                cur_len += 1
                cur_num += 1
            max_len = max(max_len, cur_len)

    return max_len


# test case
nums = [100, 4, 200, 1, 3, 2, 2]
print('test case for hash map:')
print(longestConsecutive(nums))  # 4


# 3. hash_map --> set
def longestConsecutive(nums):
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if num - 1 not in num_set:  # 找到序列的起点
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            max_len = max(max_len, current_streak)

    return max_len

# test case
nums = [100, 4, 200, 1, 3, 2, 2]
print('test case for hash map:')
print(longestConsecutive(nums))  # 4




        
