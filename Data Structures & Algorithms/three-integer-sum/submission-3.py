class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        t = 0

        # -4, -3, -2, 0, 1, 2
        # -3 + 2 = -1
        # -1 > -4
        
        while t < len(nums) - 2:

            if t > 0 and nums[t] == nums[t - 1]:
                t += 1
                continue
            
            i = t + 1
            j = len(nums) - 1
            while i < j:

                if nums[i] + nums[j] > -nums[t]:
                    j -= 1
                    continue
                elif nums[i] + nums[j] < -nums[t]:
                    i += 1
                    continue
                else:
                    res.append([nums[i], nums[j], nums[t]])
                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
            
            t += 1

        return res