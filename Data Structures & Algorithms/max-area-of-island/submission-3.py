class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        count = 0
        visited = set()


        def dfs(r, c):
            
            if r >= len(grid) or r < 0:
                return 0
            if c >= len(grid[0]) or c < 0:
                return 0
                
            if grid[r][c] == 0:
                return 0      
            if (r, c) in visited:
                return 0
            visited.add((r, c))

            a = 1
            a += dfs(r + 1, c)
            a += dfs(r - 1, c)
            a += dfs(r, c + 1)
            a += dfs(r, c - 1)
            return a
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = max(count, dfs(i, j))

        return count