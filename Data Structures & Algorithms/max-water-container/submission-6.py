class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # distance * min(heights)
        # keep moving the pointer with the shorter length

        lp = 0
        rp = len(heights) - 1
        max_container = float('-inf')

        while lp < rp:
            max_container = max((rp - lp) * min(heights[lp], heights[rp]),
                                max_container)
            if heights[lp] < heights[rp]:
                lp += 1
            elif heights[lp] > heights[rp]:
                rp -= 1
            else:
                lp += 1
                rp -= 1
        
        return max_container