class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_count = 0
        visited = set()

        def dfs(r, c):
    
            if r < 0 or r >= len(grid):
                return 0 
            if c < 0 or c >= len(grid[0]):
                return  0         
            if (r, c) in visited:
                return 0 
            
            if grid[r][c] == 1:
                visited.add((r, c))
            else:
                return 0
        
            # we will always add one here
            #if we return a at the end it will return in the end of the call stack
            #we do not keep track of a count variable, we simply just check the max after each iteration
            a = 1
            a += dfs(r + 1, c)
            a += dfs(r - 1, c)
            a += dfs(r, c + 1)
            a += dfs(r, c - 1)
            return a
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_count = max(max_count, dfs(i, j))
        
        return max_count





