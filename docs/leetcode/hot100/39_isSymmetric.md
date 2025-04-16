# 对称二叉树问题解题思路与心得

## 问题描述
给定一个二叉树的根节点 root，检查它是否轴对称。即从根节点画一条垂直线，树的左右两边是否互为镜像。

## 解题思路的演进

### 第一个思路：对称化后比较
最初的想法是：
1. 先把其中一棵子树对称化
2. 然后判断两棵树是否完全相同

这个思路源于一个直觉：判断两棵树是否完全相同似乎比判断是否互为镜像更简单。但通过深入分析发现这是一个误导性的直觉。

### 关键突破：算法复杂度的对比分析

让我们对比两种算法的核心逻辑：

```python
# 判断两棵树完全相同
def isSameTree(left, right):
    if not left and not right: return True
    if not left or not right: return False
    return (left.val == right.val and 
            isSameTree(left.left, right.left) and    # 左对左
            isSameTree(left.right, right.right))     # 右对右

# 判断两棵树互为镜像
def isMirror(left, right):
    if not left and not right: return True
    if not left or not right: return False
    return (left.val == right.val and 
            isMirror(left.left, right.right) and     # 左对右
            isMirror(left.right, right.left))        # 右对左
```

这个对比让我们发现：
1. 两个算法的复杂度是完全相同的
2. 唯一的区别仅仅是递归调用时节点的对应关系不同
3. 因此，先对称化再比较完全相同反而增加了不必要的步骤

### 第二个思路：使用栈/队列的混淆
在考虑迭代解法时，出现了对数据结构使用的混淆：
1. 最初想到使用栈（stack）来做遍历
2. 但实际上层序遍历更适合使用队列（queue）
3. 这个混淆部分源于对层序遍历的不熟悉

## 队列解法的正确实现
```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        dq = [(root.left, root.right)]

        while dq:

            left, right = dq.pop(0)

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val:
                return False
            
            dq.append((left.left, right.right))
            dq.append((right.left, left.right))

        return True
```

## 关键心得

1. **算法复杂度的直觉可能具有误导性**：
   - 不要想当然地认为某种方法更简单
   - 应该通过实际的代码对比来判断复杂度

2. **数据结构的选择陷阱**：
   - 栈（Stack）：后进先出，适合深度优先搜索
   - 队列（Queue）：先进先出，适合层序遍历
   - 在树的遍历问题中，应该根据遍历方式选择合适的数据结构

3. **化繁为简的思维方式**：
   - 直接判断镜像关系比"先对称化再判断相同"更简单
   - 有时候看似更直接的方法反而会增加复杂度

这个问题很好地说明了在算法设计中，我们常常需要：
- 突破直觉带来的思维定式
- 正确理解和使用数据结构
- 通过实际的代码分析来判断方法的优劣

解决这类问题的关键不在于记忆具体的解法，而是培养对算法复杂度的正确认识，以及对基本数据结构特性的准确理解。