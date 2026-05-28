class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        print(freq)

        s_freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)

        final_freq = s_freq[:k]

        res = []
        for i in final_freq:
            res.append(i[0])

        return res

    
