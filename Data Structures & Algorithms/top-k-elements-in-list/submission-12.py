class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # the main goal here is to understand this lambda stuff
        # and understadn the sorted function and what it can have
        # first we pick what we are sorting
        # then we define what we are choosing to sort
        
        def getVal(pair):
            return pair[1]
        freq = Counter(nums)

        top_freq = sorted(freq.items(), key=getVal, reverse=True)
        #top_freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)
        

        res = []
        for i in range(k):
            res.append(top_freq[i][0])

        return res