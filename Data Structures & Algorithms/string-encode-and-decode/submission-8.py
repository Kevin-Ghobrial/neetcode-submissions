class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        
        return res

    def decode(self, s: str) -> List[str]:

        print(s)
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i : j])
            jump = int(s[i:j])
            start = j + 1
            end = start + jump
            substr = s[start: end]
            res.append(substr)
            #print(jump, start, end, substr)
            i = end
        
        return res
