class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1, 2, 4, 6
        # (2 * 4 * 6), (1 * 4 * 6)

        # without zeros

        # -1, 0, 1, 0, 3
        # if there are > 1 zeros the entire array will be zero

        zeroCount = 0
        zeroInx = 0
        total = 1
        isZero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                isZero = True
                zeroCount += 1
                zeroInx = i
                if zeroCount > 1:
                    return [0] * len(nums)
                continue
            total *= nums[i]
        
        
        if isZero:
            res = [0] * len(nums)
            res[zeroInx] = total
            return res
        else:
            res = []
            for i in nums:
                res.append(total // i)
            return res



        
            