class Solution:
    def solve(self, board: List[List[str]]) -> None:
    
        # check boarder for O
        # do a dfs and mark all O connected
        # run through graph and make everything else an X

        q = deque()
        visited = set()
        sur = [[True] * len(board[0]) for _ in range(len(board))]

        for r in range(len(board)):
            if board[r][0] == "O":
                q.append((r, 0))
                sur[r][0] = False
                visited.add((r, 0))
            if board[r][len(board[0]) -1] == "O":
                q.append((r, len(board[0]) - 1))
                sur[r][len(board[0]) -1] = False
                visited.add((r, len(board[0]) -1))

        for c in range(len(board[0])):
            if board[0][c] == "O":
                q.append((0, c))
                sur[0][c] = False
                visited.add((0, c))
            if board[len(board) - 1][c] == "O":
                q.append((len(board) - 1, c))
                sur[len(board) - 1][c] = False
                visited.add((len(board) - 1, c))
        
        diri = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            
            for dr, dc in diri:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= len(board):
                    continue
                if nc < 0 or nc >= len(board[0]):
                    continue
                if (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                if board[nr][nc] == "O":
                    sur[nr][nc] = False
                    dfs(nr, nc)
        
        for _ in range(len(q)):
            r, c = q.popleft()
            dfs(r, c)
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if sur[i][j] == True:
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
        





