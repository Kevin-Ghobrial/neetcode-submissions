class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        minBuy = prices[0]

        for s in prices:
            maxP = max(maxP, s - minBuy)
            minBuy = min(minBuy, s)
        
        return maxP
            
