from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0


        res = {} # key 是当前连续序列的起点的最大连续序列长度.
        

        for x in nums:
            if x not in res:
                res[x] = 1
            
            y = x + 1
            while y in nums:
                res[x] += 1
                y += 1
            
        return max(res.values())


if __name__ == "__main__":
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
