class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        maxVal = 0

        for i in nums:
            if i - 1 not in numSet:
                cur = i
                curVal = 1
                while cur + 1 in numSet:
                    curVal += 1
                    cur += 1
                maxVal = max(curVal, maxVal)

        return maxVal