class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        
        while (lp <= rp):
            # l+r // 2 can lead to overflow
            mid = lp + ((rp - lp ) // 2)
            #print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lp = mid + 1
            else:
                rp = mid - 1
        
        
        return -1
            