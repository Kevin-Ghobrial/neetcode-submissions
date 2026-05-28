class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
    
        def dfs(substring, open_p, closed_p):
            if open_p == n and closed_p == n:
                res.append(substring)
                return
            
            # take open
            if open_p < n:
                dfs(substring + "(", open_p + 1, closed_p)

            # take closed
            if open_p > closed_p:
                dfs(substring + ")", open_p, closed_p + 1)
        
        dfs("", 0, 0)
        return res