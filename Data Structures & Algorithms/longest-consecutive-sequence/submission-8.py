class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        # works going forward, what about backword
        # 2, 20, 3, 10, 4
        # 2, 3
        # cache? for that variables current count
        # cache needs to be hashtable, with num as key, count as value
        # set for O(1) look up time

        # since value is int
        cache = defaultdict(int)
        nums_set = set()

        for i in nums: # -> O(n)
            if i not in nums_set:
                cache[i] += 1
                nums_set.add(i)

        
        # 2, 20, 3, 10, 4
        # {2: 1, 20: 1, 3: 1, 10: 1, 4: 1}
        # 0, 3, 2, 5, 4, 6, 1, 1
        for i in nums:
            if (i - 1) in nums_set:
                cache[i] = cache[i - 1] + 1
            elif (i + 1) in nums_set:
                j = i
                while (j + 1) in nums_set:
                    cache[j + 1] = cache[j] + 1
                    j += 1
        
        return max(cache.values())



