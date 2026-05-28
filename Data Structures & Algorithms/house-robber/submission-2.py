class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])


        dp = [0] * len(nums)

        dp[len(nums) - 1] = nums[len(nums) - 1]
        dp[len(nums) - 2] = nums[len(nums) - 2]

        print(dp)

        for i in range(len(dp) - 3, -1, -1):
            if i + 2 < len(dp):
                dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        
        print(dp)
        print(dp[0], dp[1])
        return max(dp[0], dp[1])


