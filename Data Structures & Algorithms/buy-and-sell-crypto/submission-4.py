class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lp = 0
        rp = 1
        profit = 0

        while rp < len(prices):
            
            if prices[rp] - prices[lp] > 0:
                p = prices[rp] - prices[lp]
                profit = max(p, profit)
            else:
                # common 2 pointer concept here
                lp = rp 
            
            rp += 1
        
        return profit