class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == ".":
                    continue
                
                # rows and cols
                if (board[i][j] in rowMap[i]) or (board[i][j] in colMap[j]):
                    return False
                
                # square

                square = (i // 3, j // 3)
                print(square)

                if board[i][j] in squareMap[square]:
                    return False
                

                rowMap[i].add(board[i][j])
                colMap[j].add(board[i][j])
                squareMap[square].add(board[i][j])
        
        return True

