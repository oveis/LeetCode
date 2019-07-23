class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses
        
        for (i, j) in prerequisites:
            graph[i].append(j)
            
        for course in range(numCourses):
            if not self.dfs(course, graph, visit):
                return False
            
        return True
    
    
    def dfs(self, course, graph, visit):
        if visit[course] == -1:
            return False
        elif visit[course] == 1:
            return True
        
        visit[course] = -1
        
        for pre in graph[course]:
            if not self.dfs(pre, graph, visit):
                return False
        
        visit[course] = 1
        return True
