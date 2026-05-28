class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums) - 1)

        # with last index
        dp1[len(nums) - 2] = nums[len(nums) - 1]
        dp1[len(nums) - 3] = max(nums[len(nums) - 1] , nums[len(nums) - 2])

        # with 0 index
        dp2[len(nums) - 2] = nums[len(nums) - 2]
        dp2[len(nums) - 3] = max(nums[len(nums) - 2] , nums[len(nums) - 3])

        for i in range(len(dp1) - 3, -1, -1):
            print(dp1)
            print(dp2)
            if i != 0:
                dp1[i] = max(dp1[i + 1], nums[i + 1] + dp1[i + 2])
            else:
                dp1[i] = max(dp1[i + 1], nums[i + 1] + dp1[i + 2])
            dp2[i] = max(dp2[i + 1], nums[i] + dp2[i + 2])
        

        print(dp1)
        print(dp2)
        return max(dp1[0], dp2[0])
