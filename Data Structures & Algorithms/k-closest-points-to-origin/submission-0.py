class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minDist = math.sqrt((100)**2 + (100)**2)
        minHeap = []
        heapq.heapify(minHeap)


        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(minHeap, (dist, x, y))
        
        res = []
        
        for _ in range(k):
            dist, i, j = heapq.heappop(minHeap)
            res.append([i, j])
            
        
        return res

        
                