class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for i in nums:
            if i not in dup:
                dup[i] = 1
            else:
                return True

        return False