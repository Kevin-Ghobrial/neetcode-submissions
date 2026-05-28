class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                c = board[i][j]
                if c == ".":
                    continue
            
                # row
                if c in rows[i]:
                    return False
                rows[i].add(c)

                # column
                if c in cols[j]:
                    return False
                cols[j].add(c)

                #square

                # [4, 4]
                # 4 // 3 -> [1, 1]

                #idea: get every index and divide by 3, that will give us the correct square
                # squares will hold a tuple as key
                index = (i // 3, j // 3)
                if c in squares[index]:
                    return False
                squares[index].add(c)
        
        return True





