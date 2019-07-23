class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses
        
        for (i, j) in prerequisites:
            graph[i].append(j)
        
        ans = []
        for course in range(numCourses):
            if not self.dfs(course, graph, visit, ans):
                return []
        return ans
    
    
    def dfs(self, course, graph, visit, ans):
        if visit[course] == -1:
            return False
        elif visit[course]:
            return True
        
        visit[course] = -1
        
        for pre in graph[course]:
            if not self.dfs(pre, graph, visit, ans):
                return False
        
        visit[course] = 1
        ans.append(course)
        return True
