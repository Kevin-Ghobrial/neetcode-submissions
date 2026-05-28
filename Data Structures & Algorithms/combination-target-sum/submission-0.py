class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #every subset with its sum hashmap

        res = []
        subset = []
        nums.sort()

        def dfs(i, t):
            if t == target:
                res.append(subset.copy())
                return
            if i == len(nums) or t > target:
                return
            
            #take it
            subset.append(nums[i])
            dfs(i, t + nums[i])

            #dont take it
            subset.pop()
            dfs(i + 1, t)
        
        dfs(0, 0)
        return res
