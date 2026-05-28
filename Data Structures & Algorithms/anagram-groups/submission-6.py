class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        sublist = defaultdict(list)

        for s in strs:
            s_s = sorted(s)
            sublist[str(s_s)].append(s)
        
        for i in sublist.values():
            res.append(i)
        
        return res