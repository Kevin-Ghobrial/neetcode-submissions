class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        if sum(gas) < sum(cost):
            return -1

            
        tank = 0
        res = 0
        # 1, 2, 3, 4
        # 2, 2, 4, 1

        # 
        
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])

            # if we could reach i without tank going to zero, that means
            # we we can simply set res to i + 1 as the start
            # assuming we can make a full loop 
            if tank < 0:
                tank = 0
                res = i + 1

        return res