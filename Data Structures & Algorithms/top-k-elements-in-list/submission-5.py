class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # gives us a hashmap of the frequencies of each element
        freq = Counter(nums)
        
        freq_s = sorted(freq.items(), key=lambda item: item[1], reverse = True)

        res = []
        for i in range(k):
            print(freq_s)
            res.append(freq_s[i][0])
        
        return res
