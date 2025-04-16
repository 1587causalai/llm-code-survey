# 46. 全排列


想到递归我感觉就解决问题了。

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 递归方法
        if len(nums) <= 1:
            return [nums]
        n = len(nums)

        res_prev = self.permute(nums[:-1])
        res = []
        for lst in res_prev:
            for i in range(n):
                tmp = lst.copy()
                tmp.insert(i, nums[-1])
                res.append(tmp)

        return res

            


```
