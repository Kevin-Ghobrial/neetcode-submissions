class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        lp = 0
        rp = k - 1

        h = defaultdict(int)
        for i in range(k):
            if blocks[i] == "W":
                h["W"] += 1
            elif blocks[i] == "B":
                h["B"] += 1
        
        if h["B"] == k:
            return 0
        
        print(h)

        recolors = h["W"]
        while rp < len(blocks) - 1:
            rp += 1
            h[blocks[rp]] += 1
            h[blocks[lp]] -= 1
            lp += 1
                

            recolors = min(recolors, h["W"])

        return recolors            
            
