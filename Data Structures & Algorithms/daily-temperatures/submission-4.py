class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # idea: create a stack which will store the temps and index
        # go through the stack, and compare a new variable to it
        # see if that new variable has a greater temp
        # store newI - i in the arr

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append((t, i))
        
        return res

