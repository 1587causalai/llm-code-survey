# 两数相加（链表）

## 题目描述

给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。要求将两个数相加，并以相同形式返回一个表示和的链表。

可以假设除了数字 0 之外，这两个数都不会以 0 开头。

## 题目理解

这道题的关键在于理解数字在链表中的特殊存储方式：

1. 数字是倒序存储的
2. 每个节点只存储一位数字
3. 需要处理进位问题

举例说明：
- 数字 342 在链表中表示为：`2 -> 4 -> 3`
- 数字 465 在链表中表示为：`5 -> 6 -> 4`
- 它们的和 807 应表示为：`7 -> 0 -> 8`

## 解法分析

### 解法一：清晰直观版本

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0  # 进位

        while l1 or l2:
            # 获取当前位的值
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # 计算和与进位
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            
            # 创建新节点
            cur.next = ListNode(digit)
            cur = cur.next

            # 移动到下一个节点
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # 处理最后可能的进位
        if carry:
            cur.next = ListNode(carry)

        return dummy.next
```

代码特点：
1. 使用虚拟头节点简化操作
2. 变量命名清晰：carry表示进位，cur表示当前节点
3. 逻辑分块明确，易于理解和维护
4. 单独处理最后的进位情况

### 解法二：简洁版本

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = s = ListNode()
        k = 0
        while l1 or l2 or k:
            if l1:
                k += l1.val
                l1 = l1.next
            if l2:
                k += l2.val
                l2 = l2.next
            n.next = ListNode(k%10)
            k = k//10
            n = n.next
        return s.next
```

代码特点：
1. 代码更简洁
2. 使用k同时作为进位和累加器
3. 通过在循环条件中加入k，巧妙处理最后的进位
4. 逻辑更加紧凑但可读性略差

## 两种解法的比较

1. 代码结构：
   - 解法一结构清晰，逻辑分块明确
   - 解法二代码更简洁，但逻辑略显混乱

2. 变量命名：
   - 解法一使用carry, cur等有意义的变量名
   - 解法二使用k, n等简短但含义不明确的变量名

3. 可维护性：
   - 解法一更易于维护和修改
   - 解法二虽然简洁，但不易于扩展

4. 实际应用：
   - 在实际工作中，推荐使用解法一的风格
   - 解法一的风格更符合工程实践的要求

## 复杂度分析

- 时间复杂度：O(max(len(l1), len(l2)))
  - 需要遍历完两个链表中较长的那个
  
- 空间复杂度：O(max(len(l1), len(l2)))
  - 需要创建一个新链表存储结果

## 总结

这道题的核心在于：
1. 理解逆序存储的特点
2. 正确处理进位
3. 考虑边界情况

在实际编程中，应该在代码简洁性和可读性之间找到平衡，优先保证代码的可维护性和可理解性。