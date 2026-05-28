class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # move right pointer right until condition fails
        # move left pointer right until condition passes
        
        freq = defaultdict(int) # dict chars : count

        # condition: window - max(freq.values()) <= k

        lp = 0
        rp = 1
        freq[s[0]] += 1
        count = 1

        while rp < len(s):
            freq[s[rp]] += 1
            window = rp - lp + 1
            rp += 1
            if window - max(freq.values()) <= k:
                count = max(count, window)
            else:
                freq[s[lp]] -= 1
                lp += 1
            
        
        return count



