class Solution:
    def countSubstrings(self, s: str) -> int:
        # idea: increasing window sizes
        # start with window size 1, check if palindrom
        # then 2, and check, up until we are at the full size


        count = len(s)
        
        # abc
        # aaa
        # lp = 0, rp = 1
        
        # first loop for size of window
        for i in range(1, len(s)):
            # second loop goes through s
            for j in range(len(s)):
                lp = j
                rp = lp + i
                if rp >= len(s):
                    break
                if s[lp] != s[rp]:
                    continue
                else:
                    while s[lp] == s[rp]:
                        lp += 1
                        rp -= 1
                        if lp >= rp:
                            count += 1
                            break
        
        return count


                

                
            
