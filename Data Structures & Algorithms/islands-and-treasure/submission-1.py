class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        q = deque()
        diri = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:

            r, c = q.popleft()
            for dr, dc in diri:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= len(grid):
                    continue
                if nc < 0 or nc >= len(grid[0]):
                    continue
                    
                if grid[nr][nc] == inf:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
    
