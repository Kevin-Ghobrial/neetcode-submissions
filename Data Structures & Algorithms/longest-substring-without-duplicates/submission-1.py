class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        lp = 0
        rp = 1

        # pwwkew
        # pw, pww

        dup = set()
        dup.add(s[lp])

        count = 1
    
        while rp < len(s):
            if not s[rp] in dup:
                dup.add(s[rp])
                count = max(count, rp - lp + 1)
                rp += 1
            else:
                while rp >= lp and s[rp] in dup:
                    dup.remove(s[lp])
                    lp += 1
        
        return count
            

            





