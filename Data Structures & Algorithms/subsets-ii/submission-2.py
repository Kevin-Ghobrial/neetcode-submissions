class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        made = set()

        def dfs(i, subset):
            if i >= len(nums):
                if tuple(subset.copy()) not in made:
                    made.add(tuple(subset.copy()))
                    res.append(subset.copy())
                return
            
            # take
            subset.append(nums[i])
            dfs(i + 1, subset)

            #don't take
            subset.pop()
            dfs(i + 1, subset)
        
        dfs(0, [])
        return res