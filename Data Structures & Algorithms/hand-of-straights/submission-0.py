class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # return False if its impossible to split the cards evenly

        if len(hand) % groupSize != 0:
            return False

        #hashmap of values in hand
        count = Counter(hand)

        # {1: 1, 2: 2, 3: 2, 4:2, 5: 1}
        for i in sorted(count.keys()):
            
            k = count[i]
            
            if k == 0:
                continue
            
            for c in range(i, i + groupSize):

                if count[c] < k:
                    return False
                
                count[c] -= k
        
        return True

