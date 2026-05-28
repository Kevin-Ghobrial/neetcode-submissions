class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        diri = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            r, c = q.popleft()

            for dr, dc in diri:
                nr = r + dr
                nc = c + dc

                if 0 > nr or nr >= len(grid):
                    continue
                if 0 > nc or nc >= len(grid[0]):
                    continue
                
                if grid[nr][nc] == inf:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        
