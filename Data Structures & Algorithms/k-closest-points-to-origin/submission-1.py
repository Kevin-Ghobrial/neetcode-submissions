class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #minDist = math.sqrt(100)**2 + math.sqrt(100)**2
        stack = []
        heapq.heapify(stack)

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(stack, (dist, x, y))
        
        res = []
        for _ in range(k):
            sol = heapq.heappop(stack)
            res.append([sol[1], sol[2]])
        
        return res