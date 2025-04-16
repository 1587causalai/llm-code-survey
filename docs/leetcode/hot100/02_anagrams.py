import collections


# 排序法, 字母异位词
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)

    print(ans.keys())
    return ans.values()


# test code
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))


# 哈希表法
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
            # ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
        ans[tuple(count)].append(s)

    return ans.values()

# test code
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

# 质数相乘法
def groupAnagrams(strs):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    ans = collections.defaultdict(list)
    
    for s in strs:
        product = 1
        for char in s:
            product *= primes[ord(char) - ord('a')]
        ans[product].append(s)
    
    return list(ans.values())

# test code
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))


# 位运算法
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        count = 0
        for c in s:
            count += 1 << (ord(c) - ord('a'))
        ans[count].append(s)
    return ans.values()

# test code
strs = ["eat", "tea","teae", "b", "aa"] # 所以这是一个错误的算法. 
print(groupAnagrams(strs)) # [['eat', 'tea'], ['teae'], ['b', 'aa']]


# 最终解法
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        

        return list(ans.values())
        
# test code
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(strs))