class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxA = 0
        j = len(heights) - 1
        i = 0
        while i < j:
            a = (j - i) * (min(heights[i], heights[j]))
            if a > maxA:
                maxA = a
            
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1


        return maxA


