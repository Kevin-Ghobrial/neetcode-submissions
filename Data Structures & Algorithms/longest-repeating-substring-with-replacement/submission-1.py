class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        lp = 0
        maxF = 0
        total = 0
        
        for rp in range(len(s)):
            counts[s[rp]] = 1 + counts.get(s[rp], 0)

            maxF = max(maxF, counts[s[rp]])

            while lp < len(s) and (rp - lp + 1) - maxF > k:
                counts[s[lp]] -= 1
                lp += 1

            total = rp - lp + 1
            
        return total