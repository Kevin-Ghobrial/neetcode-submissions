class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        
        lp = 0
        rp = len(n) - 1

        while lp < rp:
            
            if n[lp] + n[rp] > target:
                rp -= 1
            elif n[lp] + n[rp] < target:
                lp += 1
            else:
                return [lp + 1, rp + 1]
            
        return [0, 1]