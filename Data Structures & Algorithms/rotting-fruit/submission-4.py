class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        fresh = 0
        minute = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        
        diri = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # bfs implimentation, for each level add one to minute
        while q and fresh > 0:
            
            for _ in range(len(q)):

                r, c = q.popleft()
                for dr, dc in diri:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= len(grid):
                        continue
                    if nc < 0 or nc >= len(grid[0]):
                        continue

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            minute += 1
        
        if fresh == 0:
            return minute
        return -1





