class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # idea: we can create a stack which holds index and temperature
        # go through the temperatures. If it is greater we pop and place
        # temp_indx - stack_indx and place that in the array at stack_indx

        res = [0] * len(temperatures)
        stack = []

        # 30,38,30,36,35,40,28
        # (40, 5), (28, 6)
        # [1, 4, 1, 2, 1, 0, 0]

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                diff = i - stackI
                res[stackI] = diff
            
            stack.append((t, i))
        
        return res
            
