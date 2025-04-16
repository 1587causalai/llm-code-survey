# 柱状图中最大矩形问题详解

## 1. 问题理解

给定一个柱状图，要求在柱状图中找出能勾勒出的最大矩形面积。这个矩形的高度受限于其覆盖范围内最矮的柱子。

## 2. 解题思路演进

### 2.1 分治思路（初始方案）

最初的一个思路是使用分治法。基本思想是：
1. 找到数组中的最小值
2. 计算以这个最小值为高，整个数组长度为宽的矩形面积
3. 将数组在最小值位置分成左右两部分，递归处理
4. 返回三者中的最大值

```python
def largestRectangleArea(self, heights: List[int]) -> int:
    n = len(heights)
    if n == 0:
        return 0
    if n == 1:
        return heights[0]
    
    ind, val = 0, heights[0]
    for i, v in enumerate(heights):
        if v <= val:
            ind = i
            val = v
    
    if ind == 0:
        return max(val * n, self.largestRectangleArea(heights[1:]))
    if ind == n-1:
        return max(val * n, self.largestRectangleArea(heights[:-1]))

    left = heights[:ind]
    left = self.largestRectangleArea(left)
    right = heights[ind+1:]
    right = self.largestRectangleArea(right)

    return max(val * n, max(left, right))
```

这个解法的问题在于：
1. 时间复杂度高：每次递归都要遍历数组找最小值
2. 空间复杂度高：每次递归都要创建新的子数组
3. 在最坏情况下（数组近乎有序时），可能退化到 O(n²)

### 2.2 直观思路

最直观的思路是：对于每个柱子，我们都把它作为矩形的高度，然后向两边扩展，直到遇到比它矮的柱子，这样就能找到以这个高度能够形成的最大矩形。

```python
def largestRectangleArea(self, heights: List[int]) -> int:
    max_area = 0
    n = len(heights)
    
    for i in range(n):
        height = heights[i]
        
        # 向左找第一个比它矮的
        left = i
        while left > 0 and heights[left-1] >= height:
            left -= 1
            
        # 向右找第一个比它矮的
        right = i
        while right < n-1 and heights[right+1] >= height:
            right += 1
            
        # 计算面积
        area = height * (right - left + 1)
        max_area = max(max_area, area)
    
    return max_area
```

这个方法的时间复杂度是 O(n²)，因为对每个柱子都可能需要遍历整个数组。

### 2.2 关键优化思路

我们注意到：
1. 对每个柱子，我们都在找它左右两边第一个比它矮的柱子
2. 如果能用某种方法快速找到这两个边界，就能大幅提升效率

### 2.3 单调栈解法

关键突破：使用单调栈来维护一个特殊的序列，这个序列能帮我们快速找到每个柱子的左右边界。

```python
def largestRectangleArea(self, heights: List[int]) -> int:
    # 添加哨兵，处理边界情况
    heights = [0] + heights + [0]
    stack = [0]  # 栈中存放索引
    max_area = 0
    
    for i in range(1, len(heights)):
        # 当前柱子比栈顶索引对应的柱子矮
        while heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

## 3. 单调栈解法详解

### 3.1 核心概念

1. **单调栈的维护**：
   - 栈中存储的是索引
   - 这些索引对应的高度值是严格递增的
   - 新元素入栈前，会把所有比它大的元素都弹出

2. **栈的特性**：
   - 在任意时刻，栈中的序列代表了"还没找到右边界"的元素
   - 栈中每个元素，其左边第一个比它小的就是栈中它下面的那个元素

### 3.2 详细执行过程

以 heights = [2,1,5,6,2,3] 为例：

```
添加哨兵后：
索引：[0, 1, 2, 3, 4, 5, 6, 7]
值：  [0, 2, 1, 5, 6, 2, 3, 0]

1. i=1 (值为2)
stack = [0,1]

2. i=2 (值为1)
heights[2]=1 < heights[1]=2，出栈：
- 弹出索引1
- 高度=2
- 宽度=2-0-1=1
- 面积=2*1=2
stack = [0,2]

3. i=3 (值为5)
stack = [0,2,3]

4. i=4 (值为6)
stack = [0,2,3,4]

5. i=5 (值为2)
heights[5]=2 < heights[4]=6，出栈：
- 弹出索引4
- 高度=6
- 宽度=5-3-1=1
- 面积=6*1=6

heights[5]=2 < heights[3]=5，继续出栈：
- 弹出索引3
- 高度=5
- 宽度=5-2-1=2
- 面积=5*2=10
stack = [0,2,5]
```

### 3.3 关键点说明

1. **为什么需要哨兵**：
   - 开头的0：简化左边界的处理
   - 结尾的0：确保栈中所有元素都会被处理

2. **宽度计算**：
   - 右边界：当前遍历到的位置i
   - 左边界：新的栈顶位置stack[-1]
   - 宽度 = 右边界 - 左边界 - 1

3. **时间复杂度**：
   - O(n)：每个元素最多入栈和出栈一次

## 4. 总结

这道题展示了单调栈的经典应用：
1. 将O(n²)的暴力搜索优化到O(n)
2. 利用栈的特性来维护"第一个比当前元素小"的信息
3. 通过适当的数据结构选择，把看似复杂的问题简化

这种解法的精妙之处在于：它把"主动寻找边界"变成了"被动等待边界出现"，从而大幅提升了效率。