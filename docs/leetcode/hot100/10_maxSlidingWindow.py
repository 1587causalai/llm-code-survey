from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums or k == 0:
            return []

        res = []
        dq = []

        # 第一个窗口, 先进先出
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop() # 从队尾移除
            dq.append(i)

        res.append(nums[dq[0]])

        # 处理后续窗口
        for i in range(k, len(nums)):
            if dq and dq[0] <= i-k:
                dq.pop(0)  # 从队首移除

            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop() # 从队尾移除
            
            dq.append(i)
            res.append(nums[dq[0]])

        return res 
        


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    result = solution.maxSlidingWindow(nums, k)
    print(result)  # 输出: [3,3,5,5,6,7]
