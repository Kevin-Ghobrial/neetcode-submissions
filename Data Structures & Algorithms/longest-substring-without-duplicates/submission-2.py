class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # use a set to find the duplicate characters
        # have a lp and rp + while loop
        # go until the set has no duplicates and then index the output

        lp = 0
        rp = 0
        count = 0
        dup = set()

        # zxyzzzxy
        # lp: z
        # rp: x -> y
        # count: zx
        # dup: -, -, -, z, 
        while rp < len(s):
            if s[rp] not in dup:
                dup.add(s[rp])
                count = max(count, rp - lp + 1)
                rp += 1
            else:
                print(dup)
                while rp >= lp and s[rp] in dup:
                    dup.remove(s[lp])
                    lp += 1              
        
        return count


