class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [0] * len(prices)
        # [0, 0, 4]
        buy = 0

        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - prices[buy])
            
            if prices[i] < prices[buy]:
                buy = i
        
        return dp[-1]