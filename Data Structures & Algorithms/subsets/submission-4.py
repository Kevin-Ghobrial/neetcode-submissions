class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # idea is go down a path which takes and path which does not

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #take
            subset.append(nums[i])
            dfs(i + 1)

            #don't take
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res