class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        visited = set()
        # -1, -1, 0, 1, 2
        # target = 1
        # 2 + -1 = 1
        res = []
        for i in range(len(nums) - 1):
            target = -nums[i]
            

            for rp in range(len(nums) - 1, i + 1, -1):
                lp = i + 1
                while lp < rp - 1 and nums[lp] + nums[rp] < target:
                    lp += 1

                if nums[lp] + nums[rp] == target:
                    print(lp, rp)
                    print(nums)
                    if (-target, nums[lp], nums[rp]) not in visited:
                        visited.add((-target, nums[lp], nums[rp]))
                        res.append([-target, nums[lp], nums[rp]])
        
        return res