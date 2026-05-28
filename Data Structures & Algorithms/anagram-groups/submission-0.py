class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            s_str = ''.join(sorted(i))
            hashmap[s_str].append(i)
        
        return list(hashmap.values())

        
            
        