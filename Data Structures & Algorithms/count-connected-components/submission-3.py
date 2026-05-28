class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {i : [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        count = 0

        def dfs(node):
            visited[node] = True
            for n in graph[node]:
                if visited[n]:
                    continue
                dfs(n)


        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count
        

               