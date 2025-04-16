"""
三数之和问题的解决方案

问题描述：
给定一个整数数组 nums，找出所有和为 0 且不重复的三元组 [nums[i], nums[j], nums[k]]，
其中 i != j, i != k, j != k。

解题思路演进：

1. 最直观的思路：
   - 使用两个指针（start, end）分别指向数组两端
   - 然后用二分查找寻找第三个数
   代码可能长这样：
   ```python
   while start < end:
       target = -(nums[start] + nums[end])
       # 用二分查找寻找 target
       if found:
           res.append([nums[start], target, nums[end]])
   ```
   这个思路的问题：
   - 难以处理重复元素
   - 不容易确定该移动哪个指针
   - 二分查找的范围不好界定（会与start和end重叠）

2. 优化思路：
   - 既然两个指针不好操作，考虑固定一个数
   - 这样就把三数之和转化为一个"两数之和"的子问题
   - 对于剩余的数组，可以用双指针法解决两数之和

3. 去重策略：
   - 对于固定的第一个数：跳过已经用过的相同数字
   - 对于后面的双指针：找到一组解后，跳过相同的数字
   这样既不会漏掉解，也不会产生重复解

4. 优化细节：
   - 先对数组排序，这样相同的数字会相邻，便于去重
   - 可以根据三数之和与0的大小关系，决定移动哪个指针
   - 当固定的第一个数大于0时，可以提前结束（因为后面的数更大）
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                x, y, z = nums[i], nums[left], nums[right]
                if x + y + z == 0:
                    res.append([x, y, z])
                    left += 1
                    right -= 1
                elif x + y + z < 0:
                    left += 1
                else:
                    right -= 1

        res = [tuple(x) for x in res]
        res = set(res)
        res = [list(x) for x in res]
        return res
    
if __name__ == '__main__':
    nums = [-1, -1, 0, 2]
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)  # 输出: [[-1, -1, 2]]

"""
示例用法：
nums = [-1, -1, 0, 2]
solution = Solution()
result = solution.threeSum(nums)
print(result)  # 输出: [[-1, -1, 2]]

时间复杂度分析：
- 排序: O(nlogn)
- 双指针遍历: O(n²)
总体时间复杂度: O(n²)

空间复杂度：O(1) 或 O(n)，取决于排序算法的实现
"""