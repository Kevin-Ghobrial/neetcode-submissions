class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        diri = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = 0
        visited = set()

        def dfs(r, c):
            
            for dr, dc in diri:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nr >= len(grid):
                    continue
                if nc < 0 or nc >= len(grid[0]):
                    continue
                
                if (nr, nc) in visited:
                    continue
                
                if grid[nr][nc] == "1":
                    visited.add((nr, nc))
                    dfs(nr, nc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(visited)
                if (i, j) in visited or grid[i][j] == "0":
                    continue
                dfs(i, j)
                count += 1
        
        return count