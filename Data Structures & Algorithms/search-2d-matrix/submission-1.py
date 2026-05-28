class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea binary search on each row,
        # then binary search the columns

        lpR = 0
        rpR = len(matrix) - 1

        lpC = 0
        rpC = len(matrix[0]) - 1

        while lpR <= rpR:

            mid1 = lpR + ((rpR - lpR) // 2)

            if target < matrix[mid1][0]:
                rpR = mid1 - 1
            elif target > matrix[mid1][len(matrix[0]) - 1]:
                lpR = mid1 + 1
            else:
                while lpC <= rpC:

                    mid2 = lpC + ((rpC - lpC) // 2)

                    if target < matrix[mid1][mid2]:
                        rpC = mid2 - 1
                    elif target > matrix[mid1][mid2]:
                        lpC = mid2 + 1
                    else:
                        return True
                return False
                
        return False
        