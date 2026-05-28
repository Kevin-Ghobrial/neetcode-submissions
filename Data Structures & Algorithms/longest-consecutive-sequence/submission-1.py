class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        n_set = set(nums)
        count = 0

        print(n_set)
        # 0,3,2,5,4,6,1,1
        # 0, 1, 2, 3, 4, 5, 6

        for i in n_set:

            c = 1
            
            while i + 1 in n_set:
                c += 1
                i += 1
            
            count = max(count, c)
            print(count)
            print(c)
        
        return count


