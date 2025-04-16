# 20. 有效的括号



```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        left = {'(':0, '{':1, '[':2}
        right = {')':0, '}':1, ']':2}

        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if stack == []:
                    return False
                j = stack.pop()
                if left[j] != right[i]:
                    return False
            print(stack)

        return True if stack == [] else False

```

