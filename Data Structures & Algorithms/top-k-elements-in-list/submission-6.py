class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # idea: create a dict of all the elements
        # sort by value, and put in reverse order (so larger values first)
        # use a forloop to get the top k
        n_map = Counter(nums)

        s_map = sorted(n_map.items(), key=lambda items : items[1], reverse=True)

        res = []
        # i for position
        # 0 for item
        for i in range(k):
            res.append(s_map[i][0])
        
        return res