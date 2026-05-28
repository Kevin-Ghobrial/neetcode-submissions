class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lp = prices[0]

        for rp in prices:
            
            profit = max(profit, rp - lp)
            lp = min(lp, rp)
        
        return profit