class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        trapped = 0
        maxl = 0
        maxh = 0

        while i < j:
            if height[i] < height[j]:
                if height[i] >= maxl:
                    maxl = height[i]
                else:
                    trapped += maxl - height[i]
                i += 1
            else:
                if height[j] >= maxh:
                    maxh = height[j]
                else:
                    trapped += maxh - height[j]
                j -= 1
        
        return trapped
                