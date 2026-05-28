class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        candidates.sort()
        made = set()

        def dfs(i, t):
            if t == target and tuple(subset.copy()) not in made:
                res.append(subset.copy())
                made.add(tuple(subset.copy()))
                return
            if i == len(candidates) or t > target:
                return

            #take it
            subset.append(candidates[i])
            dfs(i + 1, t + candidates[i])

            #dont take it
            subset.pop()
            dfs(i + 1, t)
                
        dfs(0, 0)
        return res
                