class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        s_freq = sorted(freq.items(), key=lambda item : item[1], reverse = True)

        print(s_freq)

        res = []
        for i in range(k):
            res.append(s_freq[i][0])
        
        return res