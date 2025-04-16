# 从先序和中序遍历重构二叉树 - 学习笔记

## 核心原理

二叉树的重构需要同时使用先序遍历和中序遍历的特点：

1. 先序遍历特点：
   - 根节点总是第一个元素
   - 接着是左子树的所有节点
   - 最后是右子树的所有节点

2. 中序遍历特点：
   - 先是左子树的所有节点
   - 然后是根节点
   - 最后是右子树的所有节点

## 算法思路

1. 从先序遍历找到根节点（第一个元素）
2. 在中序遍历中定位根节点位置，由此可以：
   - 将中序遍历分成左子树和右子树部分
   - 根据左子树的大小，同样可以在先序遍历中确定左右子树的范围
3. 递归处理左右子树

## 代码框架

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder:  # 基本情况
        return None
        
    # 1. 找到根节点值
    root_val = preorder[0]
    
    # 2. 在中序遍历中找到根节点位置
    root_index = inorder.index(root_val)
    
    # 3. 分割左右子树
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    left_preorder = preorder[1:root_index + 1]
    right_preorder = preorder[root_index + 1:]
    
    # 4. 递归构建左右子树
    left = self.buildTree(left_preorder, left_inorder)
    right = self.buildTree(right_preorder, right_inorder)
    
    # 5. 返回根节点
    return TreeNode(root_val, left, right)
```

## 易错点提醒

1. 切片范围：
   - 前序遍历的左子树部分从索引1开始（跳过根节点）
   - 注意切片时包含和不包含的边界

2. 变量命名：
   - left_preorder 和 left_inorder 容易混淆
   - 建议使用清晰的命名规范

3. 递归调用：
   - 确保传入正确的参数对应关系
   - 特别注意不要把 preorder 错误地传给 inorder 参数

## 优化方向

1. 可以用哈希表存储中序遍历的值到索引的映射，避免重复查找
2. 可以通过传递索引范围而不是切片来优化空间复杂度
3. 可以添加参数验证，确保输入的遍历序列合法

## 时空复杂度

- 时间复杂度：O(n)，其中n是节点数量
- 空间复杂度：O(n)，主要是递归调用栈的开销

## 验证方法

可以通过以下方式验证重构的正确性：
1. 对重构的树进行先序和中序遍历
2. 比较遍历结果是否与输入序列相同