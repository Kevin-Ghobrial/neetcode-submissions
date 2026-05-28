class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = numbers
        i = 0
        j = len(n) - 1

        while i < j:

            if n[i] + n[j] > target:
                j -= 1
            elif n[i] + n[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]
        
        return [0, 1]

        