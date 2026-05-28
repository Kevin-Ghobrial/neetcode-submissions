class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, subset: List[int], nums: List[int], pick: List[bool]):
        if len(subset) == len(nums):
            self.res.append(subset.copy())
            return
        
        for i in range(len(nums)):
            if not pick[i]:

                # take 
                subset.append(nums[i])
                pick[i] = True
                self.backtrack(subset, nums, pick)

                # dont take (this is kinda crazy ngl)
                subset.pop()
                pick[i] = False
