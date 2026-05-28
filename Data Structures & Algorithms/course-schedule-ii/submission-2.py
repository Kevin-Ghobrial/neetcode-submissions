class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i : [] for i in range(numCourses)}
        res = []
        # creates graph of all courses
        for i in prerequisites:
            graph[i[1]].append(i[0])
        
        print(graph)
        canMake = True
        visiting = set()
        def dfs(course):

            if course in visiting:
                return False
            
            visiting.add(course)

            for n in graph[course]:
                if not dfs(n):
                    return False
            
            visiting.remove(course)
            
            # for topological sort, we run dfs and then reverse
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                canMake = False
        
        if not canMake:
            return []

        res.reverse()
        return res
