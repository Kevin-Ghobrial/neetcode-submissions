class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) == 0:
            return 0
        if k != 0 and len(s) == 1:
            return 1

        # idea: create a hashmap chars and their frequencies
        # in a given window we want to replace the chars that are not the most frequent
        # So we would do (len(window) - freq[char]) >= k for a valid window
        # if window is not valid, we push lp until its valid again
        freq = defaultdict(int)
        
        lp = 0
        rp = 1
        longest = 1

        freq[s[lp]] += 1


        for rp in range(1, len(s)):  
            
            freq[s[rp]] += 1

            while (rp - lp + 1) - max(freq.values()) > k:
                freq[s[lp]] -= 1
                lp += 1
            
            longest = max(longest, rp - lp + 1)
        
        return longest

