class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort numbers
        # -4, -1, -1, 0, 1, 2
        # -2, 0, 1, 1, 2
        nums.sort()
        res = set()

        i = 0
        while i < len(nums):
            tar = nums[i]
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                # -4 - 1 + 2 = - 3
                if nums[lp] + nums[rp] + tar < 0:
                    lp += 1
                elif nums[lp] + nums[rp] + tar > 0:
                    rp -= 1
                else:
                    res.add(tuple([nums[lp], nums[rp], tar]))
                    lp += 1
                    rp -= 1

            i += 1
        
        return list(res)