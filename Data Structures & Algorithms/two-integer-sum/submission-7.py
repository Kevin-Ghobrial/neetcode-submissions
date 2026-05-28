class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [3:1, 4:2, 5:3, 6:4]
        
        tar_finder = {}
        for i in range(len(nums)):
            print(tar_finder)
            j = target - nums[i]
            if j in tar_finder:
                return [tar_finder[j], i]

            tar_finder[nums[i]] = i

        return [0, 1] 