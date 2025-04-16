
# 最长非重复子串


给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。例如 s = "abcabcbb" ，则最长子串为 "abc" ，长度为 3 。


```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        max_len = 0
        left = 0
        d = {}

        for i, x in enumerate(s):
            if x not in d:
                d[x] = i
            else:
                left = d[x] + 1
                d[x] = i
                d = {k:v for k, v in d.items() if v >= left}
   
            max_len = max(max_len, i + 1 - left)

        return max_len
    def lengthOfLongestSubstring_two_pointers(self, s: str) -> int:
        if s == '':
            return 0
        
        res = 0
        left = 0
        
        while left < len(s):
            right = left + 1
            tmp = s[left:right]
            while right < len(s) and s[right] not in tmp:
                tmp = s[left:right+1]
                right += 1
            res = max(res, len(tmp))
            left += 1
        return res

if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring_two_pointers(s)
    print(result)  # 输出: 3
```
