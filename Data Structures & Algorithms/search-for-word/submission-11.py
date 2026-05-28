class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        diri = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        isSeen = False

        def bfs(r, c, i, seen):
            nonlocal isSeen
            
            print(board[r][c])
            print(i)
            if i >= len(word):
                isSeen = True
                return

            for dr, dc in diri:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= len(board):
                    continue
                if nc < 0 or nc >= len(board[0]):
                    continue
                if (nr, nc) in seen:
                    continue
                
                if board[nr][nc] == word[i]:
                    seen.add((nr, nc))
                    bfs(nr, nc, i + 1, seen)
            seen.remove((r, c))
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if board[i][j] == word[0]:
                    seen.add((i, j))
                    bfs(i, j, 1, seen)
        
        return isSeen
                
