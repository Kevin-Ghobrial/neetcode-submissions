class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        made = set()
        candidates.sort()
        
        def dfs(i, subset, total):

            if total == target and tuple(subset.copy()) not in made:
                made.add(tuple(subset.copy()))
                res.append(subset.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            # take
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])

            # don't take
            subset.pop()
            dfs(i + 1, subset, total)
        

        dfs(0, [], 0)
        return res