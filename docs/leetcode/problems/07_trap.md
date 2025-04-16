# 接雨水

## 题目描述
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

比如输入 height = [0,1,0,2,1,0,1,3,2,1,2,1] 的情况：

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 300">
    <!-- 坐标轴 -->
    <line x1="40" y1="260" x2="460" y2="260" stroke="black" stroke-width="2"/>
    <line x1="40" y1="20" x2="40" y2="260" stroke="black" stroke-width="2"/>
    
    <!-- Y轴刻度 -->
    <text x="20" y="265" font-size="12">0</text>
    <text x="20" y="225" font-size="12">1</text>
    <text x="20" y="185" font-size="12">2</text>
    <text x="20" y="145" font-size="12">3</text>
    
    <!-- 矩形柱子（每个宽度为30） -->
    <rect x="40" y="260" width="30" height="0" fill="#4CAF50"/>
    <rect x="70" y="220" width="30" height="40" fill="#4CAF50"/>
    <rect x="100" y="260" width="30" height="0" fill="#4CAF50"/>
    <rect x="130" y="180" width="30" height="80" fill="#4CAF50"/>
    <rect x="160" y="220" width="30" height="40" fill="#4CAF50"/>
    <rect x="190" y="260" width="30" height="0" fill="#4CAF50"/>
    <rect x="220" y="220" width="30" height="40" fill="#4CAF50"/>
    <rect x="250" y="140" width="30" height="120" fill="#4CAF50"/>
    <rect x="280" y="180" width="30" height="80" fill="#4CAF50"/>
    <rect x="310" y="220" width="30" height="40" fill="#4CAF50"/>
    <rect x="340" y="180" width="30" height="80" fill="#4CAF50"/>
    <rect x="370" y="220" width="30" height="40" fill="#4CAF50"/>
    
    <!-- 积水区域（蓝色半透明） -->
    <rect x="100" y="220" width="30" height="40" fill="#2196F3" fill-opacity="0.3"/>
    <rect x="160" y="180" width="30" height="40" fill="#2196F3" fill-opacity="0.3"/>
    <rect x="190" y="180" width="30" height="80" fill="#2196F3" fill-opacity="0.3"/>
    <rect x="220" y="180" width="30" height="40" fill="#2196F3" fill-opacity="0.3"/>
    <rect x="310" y="180" width="30" height="40" fill="#2196F3" fill-opacity="0.3"/>
    
    <!-- X轴刻度 -->
    <text x="50" y="280" font-size="12">0</text>
    <text x="80" y="280" font-size="12">1</text>
    <text x="110" y="280" font-size="12">2</text>
    <text x="140" y="280" font-size="12">3</text>
    <text x="170" y="280" font-size="12">4</text>
    <text x="200" y="280" font-size="12">5</text>
    <text x="230" y="280" font-size="12">6</text>
    <text x="260" y="280" font-size="12">7</text>
    <text x="290" y="280" font-size="12">8</text>
    <text x="320" y="280" font-size="12">9</text>
    <text x="350" y="280" font-size="12">10</text>
    <text x="380" y="280" font-size="12">11</text>
    
    <!-- 轴标签 -->
    <text x="250" y="295" font-size="14" text-anchor="middle">下标</text>
    <text x="10" y="140" font-size="14" text-anchor="middle" transform="rotate(-90,10,140)">高度</text>
    
    <!-- 标题 -->
    <text x="250" y="40" font-size="16" text-anchor="middle">接雨水示意图</text>
</svg>

在上图中：
- 绿色矩形表示输入数组中的柱子，每个柱子宽度为1
- 蓝色区域表示能够接住的雨水
- 总的接水量为6个单位：
  1. 下标2处可以接1个单位水（两边高度为1和2）
  2. 下标4处可以接1个单位水（两边高度为2和3）
  3. 下标5处可以接2个单位水（两边高度为2和3）
  4. 下标6处可以接1个单位水（两边高度为3和2）
  5. 下标8处可以接1个单位水（两边高度为2和2）

## 解题思路

### 方法一：分治法
这是一种基于最大值和次大值的巧妙解法。

**核心思想**：
1. 找到数组中的最高点和次高点
2. 这两个点之间的水量可以直接计算：`min(最高点,次高点) - height[i]`的总和
3. 对左右两侧递归处理

**优点**：
- 思路直观，容易理解
- 适合理解问题本质

**缺点**：
- 需要多次遍历数组找最大值
- 递归调用可能带来额外开销

### 方法二：双指针法（推荐）

这是一种更优的解法，只需要遍历一次数组。这个解法最突破常规认知的是, 需要两个指针一起遍历一个数组, 还有两个辅助指针... 辅助指针同时帮助判断该移动哪个指针和计算面积!




**核心思想**：
1. 使用左右两个指针从两端向中间移动
2. 始终移动指向较小值的那个指针
3. 通过维护左右两侧的最大高度来计算每个位置能接的水量

**技巧要点**：
- 当前位置能接的水量取决于左右两侧的最大高度中的较小值
- 如果一侧的高度较小，可以确定当前位置的储水量
- 指针移动规则保证了不会漏掉任何可能装水的位置

## 代码实现


```python

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
```


两种方法的特点比较：
1. 分治法
   - 思路更直观，容易理解
   - 通过找最大值和次大值，将问题分解成更小的子问题
   - 递归实现优雅，但性能不如双指针法
   
2. 双指针法
   - 时间复杂度更优，只需要遍历一次数组
   - 空间复杂度为O(1)，不需要额外空间
   - 实现相对简洁，但思路理解起来需要一定思考

## 易错点
1. 边界条件的处理：数组长度小于3时直接返回0
2. 初始化最大值指针时的位置选择
3. 计算水量时需要考虑负值的情况

## 复杂度分析
- 时间复杂度：O(n)，其中n是数组长度
- 空间复杂度：O(1)，只使用常数额外空间

## 相关题目
- [盛最多水的容器](problems/05_maxArea.md)：同样使用双指针技巧
- [三数之和](problems/06_threeSum.md)：双指针的另一个经典应用

## 总结
接雨水是一道经典的双指针题目，它的解法体现了以下几个重要的算法思想：
1. 双指针技巧的灵活运用
2. 空间换时间的思维方式
3. 从暴力解法到优化解法的演进过程

掌握这道题对于理解双指针技巧和动态规划都有很大帮助。 