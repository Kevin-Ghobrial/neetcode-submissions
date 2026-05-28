class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        # 1, 1, 3, 3
        # dp = [1, 1, 4, 4]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]