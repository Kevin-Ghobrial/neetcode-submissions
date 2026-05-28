class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #use the fact that it is non decreasing

        j = len(numbers) - 1
        i = 0
        while i < j:
            if numbers[i] == numbers[j]:
                continue
        
            sumi = numbers[i] + numbers[j]

            if sumi < target:
                i += 1
            elif sumi > target:
                j -= 1
            else:
                return [i + 1,j + 1]
        
        return [0, 1]
