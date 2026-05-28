class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 2:
            return 1
        
        cache = [0] * (n + 1)
        cache[0] = 1
        cache[1] = 2

        # 1, 2, 3, 5, 8, _, _

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        

        print(cache)
        return cache[n - 1]

