class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        if len(stones) == 1:
            return stones[0]
        
        for i in stones:
            heapq.heappush(maxHeap, -i)

        while len(maxHeap) > 1:
            a = -heapq.heappop(maxHeap) #largest
            b = -heapq.heappop(maxHeap) #second largest
            val = -(a - b)
            heapq.heappush(maxHeap, val)
        
        return -maxHeap[0]