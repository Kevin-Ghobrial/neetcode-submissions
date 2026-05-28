class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            lp = i + 1
            rp = len(nums) - 1

            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            
            while lp < rp:
                if nums[lp] + nums[rp] + n < 0:
                    lp += 1
                elif nums[lp] + nums[rp] + n > 0:
                    rp -= 1
                else:
                    res.append([nums[lp], nums[rp], n])
                    lp += 1
                    rp -= 1
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
                    
        return res
    