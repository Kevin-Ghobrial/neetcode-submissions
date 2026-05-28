class Solution:

    def encode(self, strs: List[str]) -> str:
        new_s = ""
        for s in strs:
            new_s += str(len(s)) + "#" + s
        
        return new_s
            
    def decode(self, s: str) -> List[str]:


        res = []
        i = 0
        while i < len(s):

            # find the jump value
            j = i
            while s[j] != "#":
                j += 1
            
            jump = int(s[i:j])
            start = j + 1
            end = start + jump
            res.append(s[start:end])
            i = end
        
        return res

