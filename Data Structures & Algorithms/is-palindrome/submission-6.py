class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        j = len(s) - 1
        # make sure they are all just letters


        for i in range(len(s)):
            if not (s[i].isalpha() or s[i].isdigit()):
                continue
            
            while not (s[j].isalpha() or s[i].isdigit()):
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False

            if i == j:
                break
            
            j -= 1
        
        return True
            