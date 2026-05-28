class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # stores i, t
        res = [0] * len(temperatures)

        # 30,38,30,36,35,40,28
        # (0, 30), 

        for i, t in enumerate(temperatures):
            
            while len(stack) > 0 and t > stack[-1][1]:
                stackI, stackT = stack.pop()
                if stackT < t:
                    res[stackI] = i - stackI
            stack.append((i, t))
        
        return res