class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i, n in enumerate(nums):
            j = target - n
            if j in prevMap:
                return [prevMap[j], i]
            prevMap[n] = i