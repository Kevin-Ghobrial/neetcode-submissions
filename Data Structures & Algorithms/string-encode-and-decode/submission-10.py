class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append("#"+str(len(s))+"#"+s)
        res = "".join(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        # #4Hello
        i = 0
        print(s)
        while i < len(s):
            print(s[i])
            l = 0
            if s[i] == "#":
                i += 1
                l = s[i]
                while s[i+1] != "#":
                    i += 1
                    l += s[i]
                l = int(l)
            begin = i + 2
            end = begin + l
            res.append(s[begin:end])
            i = end
        return res
        