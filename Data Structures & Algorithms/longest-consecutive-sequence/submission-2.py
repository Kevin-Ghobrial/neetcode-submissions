class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxVal = 0

        for i in nums:
            if i - 1 not in nums:
                cur = i
                curVal = 1
                while cur + 1 in nums:
                    curVal += 1
                    cur += 1
                maxVal = max(curVal, maxVal)

        return maxVal