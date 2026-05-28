class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        time = 0
        diri = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        fresh = 0

        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
                    
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in diri:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nr >= len(grid):
                        continue
                    if nc < 0 or nc >= len(grid[0]):
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1
        


