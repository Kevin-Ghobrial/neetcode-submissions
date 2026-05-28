class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlSet = set()
        pacSet = set()
        n_pacSet = set()
        n_atlSet = set()
        res = []
        diri = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(len(heights)):
            pacSet.add((i, 0))
            atlSet.add((i, (len(heights[0]) - 1)))
            n_pacSet.add((i, 0))
            n_atlSet.add((i, (len(heights[0]) - 1)))
        for j in range(len(heights[0])):
            pacSet.add((0, j))
            atlSet.add((len(heights) - 1, j))
            n_pacSet.add((0, j))
            n_atlSet.add((len(heights) - 1, j))
        
        def dfs(i, j, typ):
            
            for dr, dc in diri:
                nr = i + dr
                nc = j + dc

                if typ == "p" and (nr, nc) in n_pacSet:
                    continue
                if typ == "a" and (nr, nc) in n_atlSet:
                    continue                

                if nr < 0 or nr >= len(heights):
                    continue
                if nc < 0 or nc >= len(heights[0]):
                    continue
                

                
                if heights[nr][nc] >= heights[i][j]:
                    if typ == "p":
                        n_pacSet.add((nr, nc))
                    else:
                        n_atlSet.add((nr, nc))
            
                    dfs(nr, nc, typ)




        for p in pacSet:
            r, c = p
            dfs(r, c, "p")

        for a in atlSet:
            r, c = a
            dfs(r, c, "a") 

        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in n_pacSet and (r, c) in n_atlSet:
                    res.append([r, c])
        
        return res





            