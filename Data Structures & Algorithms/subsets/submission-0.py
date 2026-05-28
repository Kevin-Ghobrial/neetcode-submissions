class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]

        for i in nums:
            subset += [s + [i] for s in subset]
        
        return subset

            