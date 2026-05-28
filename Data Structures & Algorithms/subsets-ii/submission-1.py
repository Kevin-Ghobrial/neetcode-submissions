class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        subset = []
        made = set()
        nums.sort()

        def dfs(i):
            if tuple(subset) not in made:
                res.append(subset.copy())
                made.add(tuple(subset))
            if i == len(nums):
                return

            # take
            subset.append(nums[i])
            dfs(i + 1)
            # don't take
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res