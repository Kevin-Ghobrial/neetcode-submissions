class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)
        lp = 0
        maxCount = 0
        
        for rp in range(len(s)):
            freq[s[rp]] += 1

            while (rp - lp + 1) - max(freq.values()) > k:
                freq[s[lp]] -= 1
                lp += 1

            maxCount = max(maxCount, rp - lp + 1)
            
        return maxCount


