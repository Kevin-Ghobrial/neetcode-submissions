class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charToFreq = {}
        lp = 0
        total = 0
        maxF = 0

        for rp in range(len(s)):      
            
            if s[rp] not in charToFreq:
                charToFreq[s[rp]] = 1
            else:
                charToFreq[s[rp]] += 1

            maxF = max(maxF, charToFreq[s[rp]])

            while lp < len(s) and (rp - lp + 1) - maxF > k:
                charToFreq[s[lp]] -= 1
                lp += 1


            total = max(total, (rp - lp + 1))

        return total
            
                    
