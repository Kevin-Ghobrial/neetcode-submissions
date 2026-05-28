class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        # stack

        stack = [] # holds temp and index
        # we check if the curr temp is greater than the popped stack temp
        # if so we add cur_ind - stack_ind into the array at the stack ind
        res = [0] * len(temperatures)

        # (1, 38), (1, 30), (2, 36)

        for i, t in enumerate(temperatures):
            
            while len(stack) > 0 and stack[-1][1] < t:
                stack_i, stack_t = stack.pop()
                if t > stack_t:
                    res[stack_i] = i - stack_i
                else:
                    break
            
            stack.append((i, t))
        
        return res

