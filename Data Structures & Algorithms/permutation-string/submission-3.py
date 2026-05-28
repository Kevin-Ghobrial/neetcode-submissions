class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
            
        s1Dic = [0] * 26
        s2Dic = [0] * 26
        n = len(s1)

        for i in range(len(s1)):
            s1Dic[ord(s1[i]) - ord('a')] += 1
            s2Dic[ord(s2[i]) - ord('a')] += 1
        
        lp = 0
        rp = n - 1

        while rp < len(s2):

            if s1Dic == s2Dic:
                return True
            
            #remove current lp
            s2Dic[ord(s2[lp]) - ord('a')] -= 1
            #add new rp
            lp += 1
            rp += 1

            if rp < len(s2):
                s2Dic[ord(s2[rp]) - ord('a')] += 1
            
        return False



        
        # sliding window
        # create a full hashmap for both and check if equal
        

