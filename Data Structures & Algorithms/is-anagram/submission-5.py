class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_map_s = defaultdict(int)
        char_map_t = defaultdict(int)

        for i in s:
            char_map_s[i] += 1
        
        for j in t:
            char_map_t[j] += 1
        
        return True if char_map_t == char_map_s else False
            