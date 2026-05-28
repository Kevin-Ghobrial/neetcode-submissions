class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd = []
        prod = 1
        becomeOne = False
        zeroCount = 0
        zero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                zero = True
                zeroCount += 1
                continue
            else: 
               prod *= nums[i]
               becomeOne = True
        
        if not becomeOne:
            prod = 0
        
        if zeroCount > 1:
            return [0] * len(nums)

        for j in nums:
            if zero:
                if j != 0:
                    prd.append(0)
                else:
                    prd.append(prod)
            else:
                prd.append(prod // j)
        
        return prd


