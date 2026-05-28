import heapq

from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Get the frequencies of each char
        # Then go from char as key and freq as val

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for key, val in count.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                res.append(n)

        return res
                

        
