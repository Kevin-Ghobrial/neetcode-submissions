class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowMap = {i : set() for i in range(0, 9)}
        colMap = {i : set() for i in range(0, 9)}
        squareMap = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                #row
                if board[i][j] in rowMap[i]:
                    print("failed on row")
                    return False
                else:
                    rowMap[i].add(board[i][j])

                #col
                if board[i][j] in colMap[j]:
                    return False
                else:
                    colMap[j].add(board[i][j])
                
                #square
                if (i // 3, j // 3) not in squareMap:
                    squareMap[(i // 3, j // 3)] = set()
                    squareMap[(i // 3, j // 3)].add(board[i][j])
                elif board[i][j] in squareMap[(i // 3), (j // 3)]:
                    print("failed on square")
                    return False
                else:
                    squareMap[(i // 3, j // 3)].add(board[i][j])
        
        return True
                


