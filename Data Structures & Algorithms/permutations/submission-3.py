class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res
    
    def backtrack(self, subset: List[int], nums: List[int], taken: List[bool]):

        if len(subset) == len(nums):
            self.res.append(subset.copy())
            return 
        
        # idea for loop everything and then check which we have and have not taken

        for i in range(len(nums)):
            if not taken[i]:
                #take ( still crazy to me ngl )
                subset.append(nums[i])
                taken[i] = True
                self.backtrack(subset, nums, taken)

                # don't take
                subset.pop()
                taken[i] = False


