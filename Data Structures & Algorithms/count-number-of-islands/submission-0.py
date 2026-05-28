class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through graph and do dfs. simple
        
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        count = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return 
            if j < 0 or j >= len(grid[0]):
                return
            
            if visited[i][j]:
                return
            
            if grid[i][j] == '1':
                visited[i][j] = True
            else:
                return

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if not visited[i][j]:
                        dfs(i, j)
                        count += 1
                
        
        
        return count
            


                    