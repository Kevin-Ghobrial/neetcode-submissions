class Solution:

    def encode(self, strs: List[str]) -> str:
        en_str = ""
        for i in strs:
            en_str += str(len(i)) + "#" + i
        
        return en_str

    def decode(self, s: str) -> List[str]:
        de_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            de_str.append(s[i:j])
            i = j
        return de_str
            
            
            
            

        