class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowMap = {i : set() for i in range(0, 9)}
        colMap = {i : set() for i in range(0, 9)}
        squareMap = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if (i // 3, j // 3) not in squareMap:
                    squareMap[(i // 3, j // 3)] = set()
                
                #row
                if (board[i][j] in rowMap[i]) or (board[i][j] in colMap[j]) or (board[i][j] in squareMap[(i // 3), (j // 3)]):
                    
                    return False
  
                rowMap[i].add(board[i][j])
                colMap[j].add(board[i][j])
                squareMap[(i // 3, j // 3)].add(board[i][j])
        
        return True
                


