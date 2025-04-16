# 腐烂的橘子问题学习笔记

## 问题描述

在一个 `m x n` 的网格中，每个单元格可能包含：
- 0: 表示空单元格
- 1: 表示新鲜橘子
- 2: 表示腐烂的橘子

规则：每分钟，腐烂的橘子会使其四个方向（上、下、左、右）相邻的新鲜橘子腐烂。

目标：计算直到没有新鲜橘子为止所需的最小分钟数。如果无法使所有橘子腐烂，则返回 -1。

## 解决思路

### 方案一：直观遍历法

这是一个较为直观的解决方案，核心思想是：
1. 按时间推进模拟整个腐烂过程
2. 每分钟遍历整个网格，标记会腐烂的橘子
3. 当某一分钟没有新的橘子腐烂时，结束模拟
4. 最后检查是否还有新鲜橘子来决定返回值

优点：
- 思路清晰，容易理解和实现
- 代码结构简单，不需要复杂的数据结构
- 适合初学者学习和理解问题

缺点：
- 时间复杂度较高，每分钟都需要遍历整个网格
- 在大规模数据时可能效率不如BFS方法

### 方案二：BFS（广度优先搜索）

这是一个更优化的解决方案，核心思想是：
1. 将初始时所有腐烂的橘子作为起始点
2. 使用队列存储腐烂橘子的位置
3. 每一轮（分钟）处理队列中的所有橘子，将它们周围的新鲜橘子加入队列
4. 直到队列为空，表示腐烂过程结束

优点：
- 时间复杂度优化，每个格子最多被访问一次
- 空间利用更高效
- 适合处理大规模数据

缺点：
- 实现相对复杂
- 需要理解BFS算法的原理

## 关键实现细节

### 边界情况处理
两种方案都需要处理以下边界情况：
1. 网格为空时，返回0
2. 初始状态没有新鲜橘子时，返回0
3. 腐烂过程结束后还有新鲜橘子时，返回-1

### 新鲜橘子的追踪
两种方案采用不同的方式追踪新鲜橘子：
- 遍历法：每次需要重新统计新鲜橘子数量
- BFS法：维护一个计数器，每腐烂一个橘子就减一

## 完整代码实现

### 方案一：遍历法完整代码
```python
def orangesRotting(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    def count_fresh():
        # 统计新鲜橘子数量
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
        return count
    
    def rot_one_minute():
        # 标记这一分钟会腐烂的橘子
        to_rot = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:  # 找到腐烂的橘子
                    # 检查四个方向
                    for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                            to_rot.append((ni, nj))
        
        # 使标记的橘子腐烂
        for i, j in to_rot:
            grid[i][j] = 2
            
        # 返回这一分钟是否有橘子腐烂
        return len(to_rot) > 0

    # 如果一开始就没有新鲜橘子
    if count_fresh() == 0:
        return 0
        
    minutes = 0
    # 只要这一分钟有橘子腐烂，就继续模拟
    while rot_one_minute():
        minutes += 1
    
    # 检查是否还有新鲜橘子
    return minutes if count_fresh() == 0 else -1
```

### 方案二：BFS法完整代码
```python
from collections import deque

def orangesRotting(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    fresh_count = 0  # 统计新鲜橘子数量
    rotten = deque()  # 存储腐烂橘子的位置
    
    # 第一次遍历：统计新鲜橘子，找到腐烂橘子的初始位置
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                fresh_count += 1
            elif grid[i][j] == 2:
                rotten.append((i, j))
    
    # 如果没有新鲜橘子，直接返回0
    if fresh_count == 0:
        return 0
    
    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 四个方向
    
    # BFS过程
    while rotten and fresh_count > 0:
        minutes += 1
        # 当前这一分钟要处理的所有腐烂橘子
        for _ in range(len(rotten)):
            i, j = rotten.popleft()
            # 检查四个方向
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # 检查是否在边界内且是新鲜橘子
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 2  # 腐烂这个橘子
                    fresh_count -= 1  # 新鲜橘子数量减1
                    rotten.append((ni, nj))  # 加入队列，下一分钟从这里开始腐烂
    
    # 如果还有新鲜橘子，返回-1；否则返回所用的分钟数
    return minutes if fresh_count == 0 else -1
```

## 代码比较

### 遍历法示例
```python
def rot_one_minute():
    to_rot = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                # 检查四个方向
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        to_rot.append((ni, nj))
    
    # 使标记的橘子腐烂
    for i, j in to_rot:
        grid[i][j] = 2
        
    return len(to_rot) > 0
```

### BFS法示例
```python
def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    fresh_count = 0
    rotten = deque()
    
    # 初始化
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                fresh_count += 1
            elif grid[i][j] == 2:
                rotten.append((i, j))
    
    minutes = 0
    while rotten and fresh_count > 0:
        minutes += 1
        for _ in range(len(rotten)):
            i, j = rotten.popleft()
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh_count -= 1
                    rotten.append((ni, nj))
    
    return minutes if fresh_count == 0 else -1
```

## 学习心得

1. 这道题展示了同一个问题可以有多种解决方案，每种方案都有其优缺点
2. 虽然BFS方案在性能上更优，但直观遍历方案可能更适合初学者理解和实现
3. 在实际解题时，需要根据具体场景（如数据规模、性能要求等）来选择合适的方案

## 未来深入方向

1. 研究BFS在其他网格类问题中的应用
2. 探索是否可以用DFS（深度优先搜索）来解决此问题
3. 考虑如何优化空间复杂度
4. 研究类似的网格传播问题，如病毒传播、热传导等