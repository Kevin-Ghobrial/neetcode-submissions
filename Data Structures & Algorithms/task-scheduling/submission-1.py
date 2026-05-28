class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # hashmap of frequencies of each task
        count = Counter(tasks)
        # creating maxHeap to get more frequent tasks out of the way first
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        # queue to store idle time
        q = deque()
        count = 0

        #while we still have tasks that need to be complete
        while maxHeap or q:
            count += 1

            # if we have value in maxHeap
            if maxHeap:
                #val is equal to one less of frequency 
                val = 1 + heapq.heappop(maxHeap)
                # while val is not 0
                if val:
                    # we append the value and the time when this tasks will be ready
                    q.append([val, count + n])
            else:
                # if maxheap is empty we set count to the time when the next task will be ready because we have to wait that long anyway
                count = q[0][1]
            
            # if we have tasks waiting, we check if it is their time
            if q and q[0][1] == count:
                # if so then we push to the maxHeap
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return count