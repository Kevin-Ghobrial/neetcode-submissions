class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1Count = Counter(s1)
        s2Count = defaultdict(int)
        for i in range(len(s1)):
            s2Count[s2[i]] += 1
        

        lp = 0
        rp = len(s1) - 1
        while rp < len(s2):
            if s1Count == s2Count:
                print(lp, rp)
                return True
            else:
                if s2Count[s2[lp]] == 1:
                    del s2Count[s2[lp]]
                else:
                    s2Count[s2[lp]] -= 1
                lp += 1
                rp += 1
                if rp < len(s2):
                    s2Count[s2[rp]] += 1

        return False


