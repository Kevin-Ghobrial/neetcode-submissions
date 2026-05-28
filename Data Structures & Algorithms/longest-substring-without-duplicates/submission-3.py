class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lp = 0
        rp = 0
        count = 0
        dup = set()

        while rp < len(s):
            if s[rp] not in dup:
                dup.add(s[rp]) # add to dup 
                count = max(count, rp - lp + 1)
                rp += 1
            else:
                # keep moving lp until rp is not in dup
                while s[rp] in dup:
                    dup.remove(s[lp])
                    lp += 1
        
        return count