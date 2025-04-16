"""
/Users/gongqian/DailyLog/coding-practice-2024/src/hash_table/subarraySum.md 有详细说明
"""

def subarraySum(nums, k):

    if nums == []:
        return 0
    
    count = {0:1}
    res = 0
    cum_sum = 0
    for i in range(len(nums)):
        cum_sum += nums[i]
        if cum_sum - k in count:
            res += count[cum_sum - k]
        if cum_sum in count:
            count[cum_sum] += 1
        else:
            count[cum_sum] = 1
    return res

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    k = 2
    result = subarraySum(nums, k)
    print(result)  # 输出: 4
