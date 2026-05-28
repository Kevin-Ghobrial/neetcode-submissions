class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        repeats = set()
        lp = 0
        total = 0

        for rp in range(len(s)):
            while s[rp] in repeats:
                repeats.remove(s[lp])
                lp += 1
            
            repeats.add(s[rp])
            total = max(total, rp - lp + 1)

        return total 