class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use enumerate here somehow

        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack:
                prev_i, prev_t = stack[-1]
                if prev_t < t:
                    res[prev_i] = i - prev_i
                else:
                    break
                stack.pop()
            stack.append((i, t))
        
        return res