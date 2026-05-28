class Solution:
    def maxArea(self, heights: List[int]) -> int:

        h = heights
        # 1, 2, 9, 5, 4, 9, 1, 2


        # (rp - lp) * min(h[lp], h[rp])

        lp = 0
        rp = len(h) - 1

        bucket = 0

        while lp < rp:
            bucket = max(bucket, (rp - lp) * min(h[lp], h[rp]))

            if h[lp] < h[rp]:
                lp += 1
            elif h[lp] > h[rp]:
                rp -= 1
            else:
                lp += 1
                rp -= 1
        

        return bucket

