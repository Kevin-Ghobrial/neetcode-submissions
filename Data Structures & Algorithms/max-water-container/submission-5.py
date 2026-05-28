class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # newIdea: start from both ends and close in.
        # making the largest value

        n = len(heights)

        if n < 2:
            return 0

        if n == 3:
            return max(min(heights[0], heights[2]) * (2),
                       min(heights[0], heights[1]) * (1),
                       min(heights[1], heights[2]) * (1)
                    )
    
        rp = n - 1
        lp = 0
        curMax = min(heights[lp], heights[rp]) * (rp - lp)
        # min(heights[lp], heights[rp]) * (rp - lp)
        while rp > lp:
            goLeft = min(heights[lp], heights[rp - 1]) * (rp - lp - 1)
            goRight = min(heights[lp + 1], heights[rp]) * (rp - lp - 1)
            both = min(heights[lp + 1], heights[rp - 1]) * (rp - lp - 2)
            curMax = max(curMax, goLeft, goRight, both)
            if heights[rp] < heights[lp]:
                rp -= 1
            elif heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
                lp += 1
        
        return curMax


            

