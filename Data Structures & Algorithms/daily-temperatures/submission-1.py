class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            count = 1
            stopped = False
            for k in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[k]:
                    stopped = True
                    break
                else:
                    count += 1
            
            if stopped:
                dp[i] = count
            else:
                dp[i] = 0
        

        return dp
            