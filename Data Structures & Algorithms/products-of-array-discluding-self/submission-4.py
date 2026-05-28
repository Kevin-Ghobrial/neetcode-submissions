class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeroCount = 0

        totalProd = 1
        for i in nums:
            if i != 0:
                totalProd = totalProd * i
            else:
                zeroCount += 1

        res = [0] * len(nums)

        print(zeroCount)
        
        if zeroCount > 1:
            return res
        elif zeroCount == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = totalProd
        else:
            for i in range(len(nums)):
                res[i] = totalProd // nums[i]
            
        return res
        
        
