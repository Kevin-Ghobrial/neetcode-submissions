class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        if len(s) == 3:
            if s[0] == s[2]:
                return s
            elif s[0] == s[1]:
                return s[0:2]
            elif s[1] == s[2]:
                return s[1:3]
            else:
                return s[0]

        

        lp = 0
        rp = 2

        maxS = ""

        # if odd
        print(len(s))
        if len(s) % 2 != 0:
            for i in range(len(s)):
                print(maxS)
                lp = i
                rp = i + 2
                while lp >= 0 and rp < len(s):
                    if s[lp] == s[rp]:
                        print("are equal")
                        if len(maxS) == 0: 
                            maxS = s[lp:rp + 1]
                        else:
                            if len(maxS) < len(s[lp:rp + 1]):
                                maxS = s[lp:rp + 1]
        
                        lp -= 1
                        rp += 1
                    else:
                        break
        
        else:
            for i in range(len(s)):
                print(maxS)
                lp = i
                rp = i + 1
                while lp >= 0 and rp < len(s):
                    print(lp, rp)
                    if s[lp] == s[rp]:
                        print("are equal")
                        if len(maxS) == 0: 
                            maxS = s[lp:rp + 1]
                        else:
                            if len(maxS) < len(s[lp:rp + 1]):
                                maxS = s[lp:rp + 1]
                        lp -= 1
                        rp += 1
                    elif lp > 0 and s[lp - 1] == s[rp] and (rp - lp) % 2 != 0:
                        lp -= 1
                        if len(maxS) < len(s[lp:rp + 1]):
                            maxS = s[lp:rp + 1]
                    elif rp < len(s) - 1 and s[lp] == s[rp + 1] and (rp - lp) % 2 != 0:
                        rp += 1
                        if len(maxS) < len(s[lp:rp + 1]):
                            maxS = s[lp:rp + 1]
                    else:
                        break
        
        return maxS



        