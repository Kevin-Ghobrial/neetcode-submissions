class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 0:
            return 0

        if len(stones) == 1:
            return stones[0]

        if len(stones) == 2:
            if stones[0] > stones[1]:
                return stones[0] - stones[1]
            elif stones[1] > stones[0]:
                return stones[1] - stones[0]
            else:
                return 0
        
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        # will allow us to pop the two "heaviest" stones

        # 3, 7, 2 -> 4, 2 -> 2
        # 9, 3, 2, 10 -> 10, 9, 3, 2 -> 3, 2, 1 -> 1, 1
        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)

            if len(maxHeap) == 0 and s1 == s2:
                return 0

            if -s1 > -s2:
                val = (-s1 + s2)
                heapq.heappush(maxHeap, -val)
            elif -s2 > -s1:
                val = (-s2 + s1)
                heapq.heappush(maxHeap, -val)
        
        res = heapq.heappop(maxHeap)
        return -res
            
