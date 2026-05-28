class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #goal = len(nums) - 1
        dp = [len(nums) - 1] * len(nums)
        dp[len(nums) - 1] = 0

        # 2,9,1,1,1,1
        # [2, 1, 3, 2, 1, 0]
        # dp[i] = min(1 + dp[i + 1], 1 + dp[i + nums[i]])
    
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1
                continue
            dp[i] = min( 1 + dp[i + 1], 1 + dp[i + nums[i]])
        
        print(dp)
        return dp[0]