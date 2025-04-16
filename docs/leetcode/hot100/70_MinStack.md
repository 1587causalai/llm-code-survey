# 最小栈(MinStack)学习笔记

## 题目要求
实现 MinStack 类，包含以下方法：
1. `MinStack()` - 初始化堆栈对象
2. `void push(int val)` - 将元素val推入堆栈
3. `void pop()` - 删除堆栈顶部的元素
4. `int top()` - 获取堆栈顶部的元素（不删除）
5. `int getMin()` - 获取堆栈中的最小元素

## 学习过程中的关键疑惑点
1. 常见误解：以为最小元素一定在栈底
   - 错误原因：没有考虑到栈是动态变化的，当元素被pop出去后，最小值会改变
   - 解决方案：需要用辅助栈实时维护最小值

2. top() 方法的困惑
   - 疑惑点：不清楚 top() 和 pop() 的区别
   - 理解：
     - top() 只是"看一眼"栈顶元素，不会删除
     - pop() 会取出并删除栈顶元素

## 解题思路
1. 使用两个栈
   - 主栈(stack)：存储所有元素
   - 辅助栈(dummy)：同步维护最小值

2. 核心操作设计：
   - push操作：
     ```python
     if dummy为空 or 新元素 <= dummy栈顶:
         dummy也要push这个元素
     ```
   - pop操作：
     ```python
     if 主栈弹出的元素 == dummy栈顶:
         dummy也要pop
     ```
   - top操作：直接返回主栈栈顶
   - getMin操作：直接返回辅助栈栈顶

## 最终代码实现要点
```python
class MinStack:
    def __init__(self):
        self.stack = []    # 主栈
        self.dummy = []    # 辅助栈
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # 关键：新元素小于等于辅助栈顶时才入栈
        if self.dummy == [] or val <= self.dummy[-1]:
            self.dummy.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # 关键：确保dummy非空且值相等时才pop
        if len(self.dummy) > 0 and val == self.dummy[-1]:
            self.dummy.pop()

    def top(self) -> int:
        return self.stack[-1]    # 只查看不删除

    def getMin(self) -> int:
        return self.dummy[-1]    # 辅助栈顶即为最小值
```

## 技术要点与复杂度分析
1. 时间复杂度：
   - push、pop、top、getMin 操作均为 O(1)
   - 通过空间换时间的经典案例

2. 空间复杂度：
   - O(n)，其中 n 为栈中元素个数
   - 辅助栈最差情况下可能需要存储所有元素（当元素是递减序列时）

## 易错点提醒
1. pop操作时忘记处理辅助栈
2. push操作时忘记判断辅助栈是否为空
3. 误解top()方法的含义，与pop()混淆
4. 忘记在pop辅助栈之前检查长度