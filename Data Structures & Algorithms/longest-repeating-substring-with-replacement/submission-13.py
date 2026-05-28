class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # idea: slide rp until invalid
        # use a while loop to slide lp until valid again
        
        # How to tell if valid?
        # Hashmap: stores frequency of chars in window
        # it is valid as long as len(window) - MaxFreq >= k

        lp = 0
        rp = 1
        count = 0
        freq = defaultdict(int)
        freq[s[lp]] += 1

        while rp < len(s): 
            print(lp, rp)
            print(freq.items())
            freq[s[rp]] += 1
            window = rp - lp + 1
            if window - max(freq.values()) <= k:
                count = max(count, window)
            else:
                freq[s[lp]] -= 1
                lp += 1
            rp += 1

        return count

