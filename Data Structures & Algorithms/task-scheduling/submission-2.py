class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        count = 0

        print(maxHeap)

        while maxHeap or q:
            count += 1

            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)

                if val: # val not equal to 0
                    # next time it will be ready with its current value 
                    q.append([val, n + count])
            else:
                count = q[0][1]
            
            if q and q[0][1] == count:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return count
