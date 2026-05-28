class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        stack = []
        heapq.heapify(stack)

        # val, corr -> heaps use the first value

        for x, y in points:
            val = math.sqrt(x**2 + y**2)
            heapq.heappush(stack, (val, (x, y)))
        
        res = []
        for _ in range(k):
            val, corr = heapq.heappop(stack)
            res.append(list(corr))

        return res