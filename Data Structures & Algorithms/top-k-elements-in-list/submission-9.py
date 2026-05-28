class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        res = []

        freq = sorted(freq.items(), key=lambda item : item[1], reverse = True)

        for i in range(k):
            res.append(freq[i][0])
        
        return res