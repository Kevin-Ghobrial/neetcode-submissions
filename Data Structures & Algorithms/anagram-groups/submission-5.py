class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        sublists = defaultdict(list)

        for s in strs:
            s_s = sorted(s)
            sublists[str(s_s)].append(s)
        
        for s_list in sublists.values():
            res.append(s_list)
        
        return res
