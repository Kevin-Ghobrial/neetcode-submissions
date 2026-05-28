class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # idea: add all elements to a set
        # for each element we see if we can find an element 1 less than it
        # we keep updating the longest 
        # O(n)

        if len(nums) == 0:
            return 0

        nums_s = set(nums)
        longest = 1

        for i in nums:
            l = 1
            n = i
            while n - 1 in nums_s:
                l += 1
                n = n - 1

            
            longest = max(longest, l)
        
        return longest