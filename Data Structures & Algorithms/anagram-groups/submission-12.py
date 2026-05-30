class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # concept:
        # hashmap that will store chars

        # []

        anagrams = defaultdict(list)
        for s in strs:
            word_code = [0] * 26
            for c in s:
                word_code[ord(c) - ord('a')] += 1
            anagrams[tuple(word_code)].append(s)
        
        print(anagrams.values())
        return list(anagrams.values())
        
