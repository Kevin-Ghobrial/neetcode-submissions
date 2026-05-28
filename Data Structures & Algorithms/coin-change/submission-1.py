class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp table holds the min amount of coins needed to reach
        # the "target" which will just be the index of the array
        # so at index 5, the target will be 5 for it to reach
        # this is why we set the array to be of size amount
        dp = [amount + 1] * (amount + 1) 
        #dp[0] = 0 because no coins needed for a target of size 0
        dp[0] = 0

        # one loop goes through the array
        for t in range(1, amount + 1):
            # another loop goes through the coins
            for c in coins:
                # we have to make sure that coin can fit into the "target"
                # [0, 12, 12, 12, 12]
                if t - c >= 0:
                    # either its current value or 1 + the prev amount it took to reach the past target
                    dp[t] = min(dp[t], 1 + dp[t - c])
        

        # this means that we were able to reach the goal
        if dp[amount] < amount + 1:
            return dp[amount]
        else:
            return -1

