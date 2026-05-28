class Solution:
    def numDecodings(self, s: str) -> int:
        
        # dp solution
        # dp table holds max amount of combinations at a given index starting
        # from the end. So dp[0] will hold max amount of the entire string

        dp = [0] * (len(s) + 1) 
        dp[len(s)] = 1

        # 1012
        # 1111 -> 1, 1, 1, 1 or 11, 11, 
        # dp = {        3 : 1 , 4: 1}

        # 12 -> 1, 2
        # dp = [2, 1, 1]

        for i in range(len(s) - 1, -1, -1):

            if s[i] != "0":
                dp[i] = dp[i + 1]
            
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        
        return dp[0]


            
