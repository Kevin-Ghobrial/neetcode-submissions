class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        pathFound = False
        visited = set()

        if len(word) > (len(board) * len(board[0])):
            return False

        diri = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, v, pastVal):
            nonlocal pathFound

            if v == len(word):
                pathFound = True
                return
            
            for dr, dc in diri:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= len(board):
                    continue
                if nc < 0 or nc >= len(board[0]):
                    continue
                print((nr, nc), v)

                if board[nr][nc] == word[v]:
                    if pastVal == (-1, -1):
                        pastVal = (r, c)
                    else:
                        if (nr, nc) == pastVal:
                            continue
                        else:
                            pastVal = (r, c)
                        
                    
                    print((nr, nc))
                    dfs(nr, nc, v + 1, pastVal)



        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    #search entire word
                    dfs(i, j, 1, (-1, -1))
        
        return pathFound