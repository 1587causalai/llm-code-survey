# 链表相交问题详解

## 问题描述
给定两个单链表的头节点 `headA` 和 `headB`，找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 `null`。

## 关键概念理解

### 节点相等的判断
在链表中，判断两个节点是否相等是通过比较节点的引用（内存地址），而不是节点的值：

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 值相同但是不同对象的节点
node1 = ListNode(5)
node2 = ListNode(5)
print(node1 != node2)  # True，因为是不同的对象

# 指向同一个节点的指针
ptr1 = node1
ptr2 = node1
print(ptr1 != ptr2)  # False，因为指向同一个对象
```

## 解题思路演进

### 1. 最直观解法（暴力法）
```python
def getIntersectionNode_simple(headA, headB):
    while headA:
        tempB = headB
        while tempB:
            if headA == tempB:  # 找到相交点
                return headA
            tempB = tempB.next
        headA = headA.next
    return None
```
- 时间复杂度：O(m*n)
- 空间复杂度：O(1)
- 缺点：效率低

### 2. 优化思路分析
1. 观察特点：相交后的路径完全相同
2. 识别难点：两个链表长度可能不同
3. 突破点：如何让两个指针同时到达相交点？

### 3. 最终解法：双指针+互换跑道
```python
def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    ptrA = headA
    ptrB = headB
    
    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA
    
    return ptrA
```

## 算法验证

### 情况1：没有相交点
```
A: 1->2->3->null
B: 4->5->null

指针移动过程：
ptrA: 1->2->3->null->4->5->null
ptrB: 4->5->null->1->2->3->null
结果：同时到达null，返回null
```

### 情况2：完全相同的链表
```
A: 1->2->3
B: 1->2->3

指针移动过程：
ptrA: 1->2->3->1->2->3
ptrB: 1->2->3->1->2->3
结果：在第一个节点就相遇
```

### 情况3：普通相交情况
```
A: 1->2->3->4->5
B: 7->8->4->5

指针移动过程：
ptrA: 1->2->3->4->5->7->8->4(相遇点)
ptrB: 7->8->4->5->1->2->3->4(相遇点)
```

## 为什么这个算法有效？

1. 路径长度平衡
   - 设链表A长度为a，B长度为b
   - 相交部分长度为c
   - 两个指针走过的距离都是a+b
   - 必然会在第一个相交点相遇

2. 必定是第一个相交点
   - 在相交点之前，两个指针走过的路径不同
   - 一旦到达相交点，后续路径完全相同
   - 因此第一次相遇必定在第一个相交点

## 解题技巧总结

1. 从简单解法开始思考
2. 观察问题的特殊性质
3. 找到问题的关键难点
4. 思考如何克服难点
5. 寻找优雅的实现方式

这道题的精妙之处在于通过"互换跑道"的方式，巧妙地解决了链表长度不同的问题，使得两个指针必定在第一个相交点相遇（如果存在相交点的话）。虽然这个解法非常巧妙，可能很难独立想到，但是通过理解这种思维方式，对解决其他链表问题也会很有帮助。


```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        currA = headA
        currB = headB

        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        
        return currA

if __name__ == '__main__':
    # A: 1->2->3->4->5
    # B: 7->8->4->5
    headA = ListNode(1) 
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(7)
    headB.next = ListNode(8)
    headB.next.next = ListNode(4)
    headB.next.next.next = ListNode(5)

    solution = Solution()
    result = solution.getIntersectionNode(headA, headB)
    print(result)  # 输出: 4
```