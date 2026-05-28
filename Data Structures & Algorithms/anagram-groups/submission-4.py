class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # idea1: go through the list and sort each word. O(nlogn)
        #        make a sublist of each of the same words and store in a hashmap
        #        make a full list with all the words in the hashmap

        # defaultdict should use the value in the arg
        strs_map = defaultdict(list)
        for s in strs:  # O(n)
            s_s = "".join(sorted(s))
            strs_map[s_s] += [s]
        
        res = []
        for i in strs_map.values():
            res.append(i)

        return res

    