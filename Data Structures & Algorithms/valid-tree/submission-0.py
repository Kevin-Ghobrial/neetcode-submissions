class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {i : [] for i in range(n)}

        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for n in graph[node]:
                if n == parent:
                    continue
                if n in visited:
                    return False
                if not dfs(n, node):     
                    return False
        
            return True
        

        if not dfs(0, -1):
            return False
        
        return len(visited) == n