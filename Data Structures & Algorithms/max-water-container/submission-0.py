class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxA = 0

        for i in range(len(heights)):
            j = len(heights) - 1
            n = j - i
            while i < j:
                a = n * (min(heights[i], heights[j]))
                if a > maxA:
                    maxA = a

                n -= 1
                j -= 1

        return maxA


