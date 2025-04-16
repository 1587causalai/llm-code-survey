# 两数之和

给定一个整数数组 nums 和一个目标值 target，在数组中找出和为目标值的两个整数的下标。可以假设每个输入只对应一个答案，且同样的元素不能被重复利用。

比如输入 nums = [2,7,11,15], target = 9，因为 nums[0] + nums[1] = 2 + 7 = 9，所以返回 [0,1]。

这道题的思路很简单，就是一个遍历加上字典的使用技巧。我们可以边遍历边记录，对于每个数字，看看是否能找到它的那个配对数字。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return []

        visited = {}

        for i, x in enumerate(nums):
            if target - x in visited:
                start = visited[target-x]
                return [start, i]
            else:
                visited[x] = i

        return []
```

这个解法的关键点在于：
1. 使用字典来存储已经遍历过的数字及其索引，这样查找配对数字的时间是 O(1)
2. 对于当前数字 x，我们想找到 target - x，如果这个数字已经在字典中，就找到了答案
3. 如果没找到配对数字，就把当前数字 x 和它的下标 i 存入字典，等待后面的数字来配对
4. 这样我们只需要遍历一次数组，每个数字最多存储一次，查找也是常数时间

举个详细的例子：
- 假设 nums = [2,7,11,15], target = 9
- 遍历到 2：visited = {2:0}
- 遍历到 7：发现 target-7=2 在字典中，返回 [0,1]

时间复杂度是 O(n)，因为我们只需要遍历一次数组，而字典的存取操作都是 O(1)。
空间复杂度是 O(n)，主要是字典的开销，最坏情况下要存储所有数字。 