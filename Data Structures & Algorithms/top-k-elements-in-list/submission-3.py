class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n_map = Counter(nums)

        n_map = sorted(n_map.items(), key=lambda item : item[1], reverse = True)
        # 1, 2, 3

        print(n_map)
        res = []
        for i in range(k):
            res.append(n_map[i][0])
        
        return res