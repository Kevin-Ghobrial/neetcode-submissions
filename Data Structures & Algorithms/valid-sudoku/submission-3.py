class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rowMap[i]) or (board[i][j] in colMap[j]) or (board[i][j] in squareMap[(i // 3), (j // 3)]):         
                    return False
  
                rowMap[i].add(board[i][j])
                colMap[j].add(board[i][j])
                squareMap[(i // 3, j // 3)].add(board[i][j])
        
        return True
                


