class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        count = 0
        visited = set()

        for c in s:
            while c in visited:
                visited.remove(s[lp])
                lp += 1
            visited.add(c)
            count = max(count, len(visited))
        
        return count
