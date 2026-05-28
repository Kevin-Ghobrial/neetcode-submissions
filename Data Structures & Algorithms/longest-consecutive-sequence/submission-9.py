class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # idea: use a set to see if a sequence exits
        # instead of climing up, we can climb down

        seq = set()
        maxCount = 0
        for i in nums:
            count = 1
            # down
            j = i - 1
            while j in seq:
                count += 1
                j -= 1
            # up
            j = i + 1
            while j in seq:
                count += 1
                j += 1
            maxCount = max(count, maxCount)
            seq.add(i)
        
        return maxCount