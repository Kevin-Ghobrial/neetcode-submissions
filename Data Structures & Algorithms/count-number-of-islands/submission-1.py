class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        print(visited)

        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == '1' and not visited[i][j]:
                visited[i][j] = True
            else:
                return
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    islands += 1

        return islands
            