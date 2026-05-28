class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        diri = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        count = 0
        visited = set()

        def dfs(r, c):

            for dr, dc in diri:
                nr = r + dr
                nc = c + dc

                if nr >= len(grid) or nr < 0:
                    continue
                if nc >= len(grid[0]) or nc < 0:
                    continue
                
                if grid[nr][nc] == "1" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dfs(nr, nc)


        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    count += 1
        
        return count
        