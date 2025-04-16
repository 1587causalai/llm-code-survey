"""
接雨水问题的两种解法分析：

解法1: 基于最大值和次大值的分治方法
思路分析：
1. 这是一种直观的解法，基于一个关键观察：如果我们知道数组中的最大值和次大值位置，
   那么这两个位置之间的水量可以用简单的数学公式计算。
2. 因为两端都是最高点，中间区域的水量就是 min(left,right) - height[i] 的总和
3. 然后对左边和右边的区域递归处理
4. 这种方法思路直观，容易理解，但实现时需要注意边界条件

解法2: 双指针法
思路分析：
1. 使用左右两个指针从两端向中间移动
2. 关键规则：总是移动指向较小值的那个指针
3. 每个位置只会被计算一次，因为指针移动是单向的
4. 当处理某个位置时，如果它的高度小于当前这一侧见过的最大高度，
   那么它一定能装水，因为另一侧一定有足够高的柱子挡着
"""

from typing import List

class Solution:
    def trap_divide_conquer(self, height: List[int]) -> int:
        """基于最大值和次大值的分治方法"""
        if not height or len(height) < 3:
            return 0
        
        def calc_area(nums):
            """当left和right是最大的两个值时，计算中间区域的水量"""
            if len(nums) < 3:
                return 0
            left, right = nums[0], nums[-1]
            min_height = min(left, right)
            # 中间每个位置能装的水就是最小高度减去当前高度
            return sum(max(0, min_height - x) for x in nums[1:-1])

        # 找到最大值和次大值的位置
        max1, max2 = 0, 1
        if height[max1] < height[max2]:
            max1, max2 = max2, max1
            
        for i in range(2, len(height)):
            if height[i] > height[max1]:
                max2 = max1
                max1 = i
            elif height[i] > height[max2]:
                max2 = i
                
        # 确保max1在max2左边
        if max1 > max2:
            max1, max2 = max2, max1
            
        # 分治处理三个区域
        left_water = self.trap_divide_conquer(height[:max1+1])
        middle_water = calc_area(height[max1:max2+1])
        right_water = self.trap_divide_conquer(height[max2:])
        
        return left_water + middle_water + right_water
    
    def trap_two_pointers(self, height: List[int]) -> int:
        """双指针解法"""
        if len(height) <= 2:
            return 0
        left, right = 0, len(height) - 1

        left_max, right_max = 0, len(height) - 1
        res = 0

        while left < right:

            if height[left] > height[left_max]:
                left_max = left

            if height[right] > height[right_max]:
                right_max = right

            if height[left_max] <= height[right_max]:
                water = height[left_max] - height[left]
                left += 1
            else:
                water = height[right_max] - height[right]
                right -= 1

            res += water

        return res

    

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    result = solution.trap_divide_conquer(height)
    print(result)  # 输出: 6
