class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        count = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return 0
            
            if j < 0 or j >= len(grid[0]):
                return 0
            
            if visited[i][j]:
                return 0

            if grid[i][j] == 1:
                visited[i][j] = True
            else:
                return 0
            
            a = 1
            a += dfs(i + 1, j)
            a += dfs(i - 1, j)
            a += dfs(i, j + 1)
            a += dfs(i, j - 1)

            return a
            

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if not visited[i][j]:
                        count = max(count, dfs(i, j))
        
        return count
