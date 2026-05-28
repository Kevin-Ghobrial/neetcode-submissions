class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # idea start from goal. dp solution


        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        #base case
        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = 1
            
        for j in range(m - 2, -1, -1):
            dp[j][n - 1] = 1
 
        # dp recurrence
        # dp table will hold the max amount of ways we can reach goal from given index i j
        # bottom up approach

        for j in range(n - 2, -1, -1):
            for i in range(m - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        
        return dp[0][0]
