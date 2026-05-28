class Solution:

    def encode(self, strs: List[str]) -> str:
        en_str = ""
        for s in strs:
            en_str += str(len(s)) + "#" + s
        
        print(en_str)
        return en_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            jump = int(s[i:j])
            start = j + 1
            end = start + jump
            res.append(s[start:end])
            i = end
        
        return res
        
