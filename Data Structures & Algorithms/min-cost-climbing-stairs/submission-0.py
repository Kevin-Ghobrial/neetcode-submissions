class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        dp = [0] * len(cost)

        dp[len(cost) - 1] = cost[len(cost) - 1]
        dp[len(cost) - 2] = cost[len(cost) - 2]

        # build backwords
        print(dp)
        for i in range(len(dp) - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        print(dp)
        return min(dp[0], dp[1])
        



