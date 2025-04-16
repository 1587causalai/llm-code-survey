# 字母异位词分组

给你一个字符串数组，请你将所有的字母异位词组合在一起。字母异位词指的是两个字符串包含的字母相同，但排列顺序可能不同。比如 "eat" 和 "ate" 就是字母异位词。

举个例子，输入 ["eat","tea","tan","ate","nat","bat"]，输出 [["bat"],["nat","tan"],["ate","eat","tea"]]。这个输出把所有的异位词都放在了同一个子数组中。

这道题的难点在于如何高效地判断两个单词是否是字母异位词。最直观的方法是对两个单词分别排序，看是否相等，但这样需要两两比较，效率太低。我们可以用一个更巧妙的方法：把排序后的字符串作为键。

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == []:
            return [[]]

        res = {}

        for s in strs:
            curr = ''.join(sorted(s))
            if curr in res:
                res[curr].append(s)
            else:
                res[curr] = [s]
            
        return list(res.values())
```

解题的关键在于：
1. 对每个单词的字母进行排序，这样所有的异位词排序后都会得到相同的字符串
   - 比如 "eat"、"tea"、"ate" 排序后都是 "aet"
2. 用排序后的字符串作为字典的键，原单词放入对应的列表中
   - 键 "aet" 对应的值就是 ["eat","tea","ate"]
3. 最后把字典中所有的值放入一个列表返回，每个值都是一组字母异位词

举个详细的例子：
- 遍历到 "eat"：排序得到 "aet"，res = {"aet": ["eat"]}
- 遍历到 "tea"：排序得到 "aet"，已存在，加入列表，res = {"aet": ["eat","tea"]}
- 遍历到 "tan"：排序得到 "ant"，res = {"aet": ["eat","tea"], "ant": ["tan"]}
- 以此类推...

时间复杂度是 O(n * k * log k)，其中 n 是字符串数组的长度，k 是字符串的最大长度。每个字符串都要进行一次排序。
空间复杂度是 O(n * k)，需要存储所有字符串。 