class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                # gives us a unique key for each word based on the letters
                count[ord(c) - ord('a')] += 1
            
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())
