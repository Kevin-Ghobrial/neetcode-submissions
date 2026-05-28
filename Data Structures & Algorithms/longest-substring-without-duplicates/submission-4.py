class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # go right until condition fails
        # move left pointer until condition passes again
        # store largest window size


        lp = 0
        rp = 0
        dup = set()
        count = 0

        # zxyzxyz
        while rp < len(s):
            if s[rp] not in dup:
                dup.add(s[rp])
                rp += 1
                count = max(count, rp - lp)
            else:
                while lp < rp and s[rp] in dup:
                    dup.remove(s[lp])
                    lp += 1
        
        return count