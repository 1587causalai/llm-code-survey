# 字符串解码算法详解

## 问题描述
给定一个经过编码的字符串，返回它解码后的字符串。编码规则是: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。

**示例:**
```
输入: s = "3[a]2[bc]"
输出: "aaabcbc"

输入: s = "3[a2[c]]"
输出: "accaccacc"
```

## 解法一：分段处理递归解法

### 算法思路
1. 将字符串分成几个部分处理：
   - 前导字母部分
   - 数字部分
   - 括号内的部分
   - 剩余部分
2. 对括号内的内容递归处理
3. 将处理结果按规则拼接

### 代码实现
```python
class Solution:
    def decodeString(self, s: str) -> str:
        if s == '':
            return ''
            
        # 处理数字
        digits = [str(i) for i in range(10)]  # 包含0-9
        
        # 处理前导字母
        i = 0
        prev = ''
        while i < len(s) and s[i] >= 'a' and s[i] <= 'z':
            prev += s[i]
            i = i + 1
            
        if i >= len(s):
            return prev
            
        # 处理数字部分
        num = ''
        while i < len(s) and s[i] in digits:
            num += s[i]
            i = i + 1
            
        if i >= len(s):
            return prev + num
            
        # 处理括号
        start = i  # 第一个 [
        stack = ['[']
        while stack and i < len(s) - 1:
            i = i + 1
            if i < len(s) and s[i] == '[':
                stack.append(s[i])
            if i < len(s) and s[i] == ']':
                stack.pop()
        end = i
        
        if num == '':
            return prev
            
        # 递归处理括号内的内容
        tmp = self.decodeString(s[start+1:end])
        res = prev + tmp * int(num)
        
        # 处理剩余部分
        if end < len(s) - 1:
            res = res + self.decodeString(s[end+1:])
            
        return res
```

### 关键点和易错点
1. **边界条件检查**：
   - 所有的 `s[i]` 访问前必须确保 `i < len(s)`
   - 条件判断中，边界检查要放在最前面
   
2. **数字处理**：
   - digits 定义需要包含 0-9
   - 可以用更优雅的写法：`num = num * 10 + int(s[i])`
   
3. **括号匹配**：
   - 使用栈来处理嵌套括号
   - 注意边界条件的处理

## 解法二：状态机解法

### 算法思路
使用递归 + 状态机的思路，根据当前字符的类型来决定下一步操作：
- 遇到数字：累积数字值
- 遇到字母：累积字符串
- 遇到 '['：递归处理子串
- 遇到 ']'：返回当前结果

### 代码实现
```python
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            num = 0
            curStr = ''
            
            while i < len(s):
                match s[i]:
                    case '[':
                        newStr, newPos = dfs(s, i + 1)
                        curStr += num * newStr
                        i = newPos
                        num = 0
                    case ']':
                        break
                    case _ if s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    case _ if s[i].isalpha():
                        curStr += s[i]
                        i += 1
                        
            return curStr, i + 1
            
        return dfs(s, 0)[0]
```

### 两种解法对比
1. **解法一（分段处理）**：
   - 更符合人的思维方式
   - 代码结构清晰，便于理解和调试
   - 适合作为教学示例
   - 代码略长，但逻辑清晰

2. **解法二（状态机）**：
   - 代码更简洁
   - 使用状态机思想，更抽象
   - 适合工程实现
   - 理解成本较高

## 总结
1. 字符串处理问题中，边界条件的处理至关重要
2. 可以用不同的思路来解决同一个问题，要根据具体场景选择合适的解法
3. 代码简洁性和可读性需要权衡
4. 递归是处理嵌套结构的有效方法