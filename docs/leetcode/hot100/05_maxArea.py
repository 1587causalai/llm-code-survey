"""
盛最多水的容器

给定 n 个非负整数 a1,a2,...,an,每个数代表坐标中的一个点 (i, ai)。
在坐标内画 n 条垂直线,垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线,使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""
# 注意：你不能倾斜容器，n 至少是2。


# 1. 暴力解法
# 思路: 两层循环, 每次计算两个柱子之间的面积, 取最大值
# 时间复杂度: O(n^2)
def maxArea(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
    return max_area

# test code
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# 记录一下算法运行时间
import time 
start = time.time()
print(maxArea(height))
end = time.time()
print("Time: ", end - start)

# 2. 双指针法
# 思路: 两个指针分别指向头和尾, 每次移动高度较小的指针, 计算面积, 取最大值. 贪心策略如此高效 - 它帮我们省略了大量不必要的计算。
# 时间复杂度: O(n)
def maxArea(height):
    max_area = 0
    i, j = 0, len(height) - 1
    while i < j:
        curr_area = area(height, i, j)
        max_area = max(max_area, curr_area)

        # 面积取决于较小高度, 移动高度较小的指针, 非常巧妙, 减少了很多不必要的计算
        # 如果不这么做, 因为宽度一定会减少, 高度不可能超过当前的较小高度, 面积必定小于当前面积
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area

def area(height, i, j):
    return min(height[i], height[j]) * (j - i)

# test code
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))

# filename: 05_maxArea.py


