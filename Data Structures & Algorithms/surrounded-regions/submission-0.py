class Solution:
    def solve(self, board: List[List[str]]) -> None:

        q = deque()
        xSet = [[True] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            if board[i][0] == 'O':
                q.append((i, 0))
                xSet[i][0] = False
            if board[i][len(board[0]) - 1] == 'O':
                q.append((i, len(board[0]) - 1))
                xSet[i][len(board[0]) - 1] = False
        
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                q.append((0, j))
                xSet[0][j] = False
            if board[len(board) - 1][j] == 'O':
                q.append((len(board) - 1, j))
                xSet[len(board) - 1][j] = False
        
        diri = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in diri:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= len(board):
                    continue
                if nc < 0 or nc >= len(board[0]):
                    continue
                
                if board[nr][nc] == 'O' and xSet[nr][nc]:
                    q.append((nr, nc))
                    xSet[nr][nc] = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if xSet[i][j]:
                    board[i][j] = 'X'
        
   
