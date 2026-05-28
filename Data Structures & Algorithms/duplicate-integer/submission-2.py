class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        # idea, run through the list, adding each new element to the dict
        # and then updating the values in the dict. If any equals two then
        # we return true. If we finish the loop we return false
        for n in nums:
            if n in map:
                return True
            else:
                map[n] = 1
        
        return False