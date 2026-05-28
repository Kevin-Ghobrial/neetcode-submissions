class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(openP, closeP, path):
            
            if openP == n and closeP == n:
                res.append(path)
                return
            
            # we can only add closed if open is here
            # openP >= closed

            if openP < n:
                dfs(openP + 1, closeP, path + '(')
            if closeP < n and closeP < openP:
                dfs(openP, closeP + 1, path + ')')
        
    
        dfs(0, 0, "")

        return res


        