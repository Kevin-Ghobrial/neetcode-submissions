class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        # two different approaches, one for even and one for odd
        # we start at the center and expand outwards

        for i in range(len(s)):

            # for even
            lp = i
            rp = i
            while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                count += 1
                lp -= 1
                rp += 1
            

            # for odd
            lp = i
            rp = i + 1
            while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                count += 1
                lp -= 1
                rp += 1
        
        return count