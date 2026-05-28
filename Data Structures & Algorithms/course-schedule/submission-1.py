class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # idea create a graph 
        # return false if there are cycles

        # creates a graph with index as key and empty list for neighbors
        graph = {i : [] for i in range(numCourses)}

        # sets all neighbors
        for i in prerequisites:
            graph[i[1]].append(i[0])

        print(graph)

        visiting = set() # if we go down a path and find a node we already hit, then we return false
        def dfs(course):

            # finds cycles
            if course in visiting:
                return False


            visiting.add(course)
            
            for n in graph[course]:
                if not dfs(n):
                    return False
            
            visiting.remove(course)
            
          
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
    
