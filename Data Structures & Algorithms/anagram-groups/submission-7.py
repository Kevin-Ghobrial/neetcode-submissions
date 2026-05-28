class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        chars = defaultdict(list)

        for s in strs:
            curChars = [0] * 26
            for c in s:
                curChars[ord(c) - ord('a')] += 1
            
            chars[tuple(curChars)].append(s)
        
        res = []
        for i in chars.values():
            res.append(i)
        
        return res

