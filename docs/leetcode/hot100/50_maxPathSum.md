# 二叉树中的路径问题解题笔记

## 问题引入
在解决二叉树路径问题时，我最初联想到了最大连续子序列和问题。这个联系很自然，因为两者都需要考虑"是否要和前面的部分连接"这个核心问题。

## 解题过程与思考

### 第一次尝试
我的第一版代码采用了分治的思路：
```python
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    if not root:
        return float('-inf')

    # 过 root 路径
    val1 = self.depth(root.left) + root.val + self.depth(root.right)
    # 不过 root 路径
    val2 = max(self.maxPathSum(root.left), self.maxPathSum(root.right))
    
    return max(val1, val2)
```

这个方案在处理 [2,-1] 这样的用例时出现了问题。原因在于处理空节点时返回 float('-inf') 导致路径和计算出现错误。

### 第二次尝试
修改了处理方式，更细致地考虑了与子树的连接情况：
```python
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    if not root:
        return float('-inf')

    val1 = root.val 
    if root.left:
        val1 = max(val1, val1 + self.depth(root.left))
    if root.right:
        val1 = max(val1, val1 + self.depth(root.right))

    val2 = max(self.maxPathSum(root.left), self.maxPathSum(root.right))
    return max(val1, val2)
```

这个版本虽然修复了问题，但存在严重的重复计算，效率较低。

### 状态定义的联系
这道题和最大连续子序列和问题有一个关键的共同点：都是通过巧妙的状态定义来简化问题。

在最大连续子序列和中：
- dp[i] 定义为：以位置i结尾的最大子序列和
- 这个定义让我们可以通过 dp[i-1] 来推导 dp[i]

在二叉树路径问题中：
- max_gain(node) 定义为：以node为起点的最大路径和
- 这个定义让我们可以通过子节点的max_gain来推导当前节点的结果

这种"以某个位置/节点结尾/开始"的状态定义技巧，是两个问题的精髓所在。

### 最终优化版本
关键突破点在于使用全局变量来记录最大路径和，这样只需要遍历一次树就能得到结果：
```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
                
            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            
            path_sum = node.val + left + right
            self.max_sum = max(self.max_sum, path_sum)
            
            return node.val + max(left, right)
            
        max_gain(root)
        return self.max_sum
```

## 解题启示

1. **全局变量的巧妙运用**：
   - 避免了函数需要同时返回多个状态的复杂性
   - 大大简化了代码结构
   - 提高了代码的可读性和维护性

2. **与动态规划的联系**：
   - 类似最大子序列和问题，都使用了"以某点为结尾/起点"的状态定义
   - 这种状态定义使得我们可以利用子问题的解来构建当前问题的解
   - 通过维护全局状态来避免重复计算
   - max_gain函数在二叉树中的作用，相当于dp数组在最大子序列和中的作用

3. **空节点处理的重要性**：
   - 初始方案中返回 float('-inf') 导致计算错误
   - 最终方案中返回 0 更合理，表示空节点不对路径和产生贡献

4. **代码优化的过程**：
   - 从朴素的分治到使用全局变量
   - 从重复计算到一次遍历
   - 思路的演进体现了算法优化的一般过程

## 类似问题拓展
这个解题技巧在其他二叉树问题中也很常见：
- 二叉树的直径
- 平衡二叉树的判定
- 二叉树的序列化

## 总结体会
在这道题中，最精彩的部分是全局变量的使用技巧。它不仅优化了时间复杂度，更重要的是大大简化了代码结构。这提醒我们，在解决复杂问题时，有时候换一个角度思考，使用一些看似简单的技巧，可能会带来意想不到的效果。