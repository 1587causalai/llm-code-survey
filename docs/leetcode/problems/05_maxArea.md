# 盛最多水的容器

给定 n 个非负整数 $a_1, a_2, ..., a_n$，每个数代表坐标中的一个点 $(i, a_i)$。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 $(i, a_i)$ 和 $(i, 0)$。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

比如输入 height = [1,8,6,2,5,4,8,3,7] 的情况：

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 300">
    <!-- 坐标轴 -->
    <line x1="40" y1="260" x2="460" y2="260" stroke="black" stroke-width="2"/>
    <line x1="40" y1="20" x2="40" y2="260" stroke="black" stroke-width="2"/>
    
    <!-- Y轴刻度 -->
    <text x="20" y="265" font-size="12">0</text>
    <text x="20" y="225" font-size="12">2</text>
    <text x="20" y="185" font-size="12">4</text>
    <text x="20" y="145" font-size="12">6</text>
    <text x="20" y="105" font-size="12">8</text>
    
    <!-- 垂直线 -->
    <line x1="80" y1="260" x2="80" y2="240" stroke="#4CAF50" stroke-width="3"/>
    <line x1="120" y1="260" x2="120" y2="100" stroke="#4CAF50" stroke-width="3"/>
    <line x1="160" y1="260" x2="160" y2="140" stroke="#4CAF50" stroke-width="3"/>
    <line x1="200" y1="260" x2="200" y2="220" stroke="#4CAF50" stroke-width="3"/>
    <line x1="240" y1="260" x2="240" y2="160" stroke="#4CAF50" stroke-width="3"/>
    <line x1="280" y1="260" x2="280" y2="180" stroke="#4CAF50" stroke-width="3"/>
    <line x1="320" y1="260" x2="320" y2="100" stroke="#4CAF50" stroke-width="3"/>
    <line x1="360" y1="260" x2="360" y2="200" stroke="#4CAF50" stroke-width="3"/>
    <line x1="400" y1="260" x2="400" y2="120" stroke="#4CAF50" stroke-width="3"/>
    
    <!-- X轴刻度 -->
    <text x="75" y="280" font-size="12">0</text>
    <text x="115" y="280" font-size="12">1</text>
    <text x="155" y="280" font-size="12">2</text>
    <text x="195" y="280" font-size="12">3</text>
    <text x="235" y="280" font-size="12">4</text>
    <text x="275" y="280" font-size="12">5</text>
    <text x="315" y="280" font-size="12">6</text>
    <text x="355" y="280" font-size="12">7</text>
    <text x="395" y="280" font-size="12">8</text>
    
    <!-- 轴标签 -->
    <text x="250" y="295" font-size="14" text-anchor="middle">下标</text>
    <text x="10" y="140" font-size="14" text-anchor="middle" transform="rotate(-90,10,140)">高度</text>
    
    <!-- 标题 -->
    <text x="250" y="40" font-size="16" text-anchor="middle">盛最多水的容器示意图</text>
    
    <!-- 最大容器示意 -->
    <line x1="120" y1="100" x2="320" y2="100" stroke="#2196F3" stroke-width="2" stroke-dasharray="5,5"/>
    <rect x="120" y="100" width="200" height="160" fill="#2196F3" fill-opacity="0.1"/>
</svg>

其中最大的容器由下标 1 和下标 8 的两条线段构成（高度分别为 8 和 7），宽度为 7，面积为 49。

注意：你不能倾斜容器，n 至少是 2。

这道题可以用双指针法来解决。对于任意两条线，容器的面积计算公式为：

$$area = \min(height[i], height[j]) \times (j - i)$$

```python
def maxArea(height):
    max_area = 0
    i, j = 0, len(height) - 1
    while i < j:
        curr_area = min(height[i], height[j]) * (j - i)
        max_area = max(max_area, curr_area)

        # 面积取决于较小高度，移动高度较小的指针. 不需要遍历所有的 (i, j) 
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area
```

解法的关键在于双指针的移动策略：
1. 初始时指针分别指向数组的两端，这样保证了最大宽度
2. 每次移动高度较小的那个指针，因为：
   - 如果移动较大的指针，宽度一定减小，而高度不可能超过当前的较小高度
   - 所以**移动较大的指针不可能得到更大的面积**, 这个贪心策略非常高效，它帮我们省略了大量不必要的计算

举个例子，对于上图中的数组：
- 初始时 i=0, j=8，面积 = $\min(1,7) \times 8 = 8$ (受限于左边高度1)
- 因为 height[0]=1 小，移动左指针，i=1, j=8，面积 = $\min(8,7) \times 7 = 49$ (最大面积)
- 以此类推...

时间复杂度是 $O(n)$，只需要遍历一次数组。
空间复杂度是 $O(1)$，只需要常数空间。