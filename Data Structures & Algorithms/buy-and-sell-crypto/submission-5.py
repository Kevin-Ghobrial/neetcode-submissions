class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lp = 0
        rp = 1
        profit = 0

        while rp < len(prices):
            cur = prices[rp] - prices[lp]
            if cur > 0:
                profit = max(cur, profit)
            else:
                lp = rp
            
            rp += 1
        
        return profit
