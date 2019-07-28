class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        
        for node in range(len(graph)):
            if node in color:
                continue
            
            stack = [node]
            color[node] = 0
            
            while stack:
                node = stack.pop()
                
                for nei in graph[node]:
                    if nei in color:
                        if color[nei] == color[node]:
                            return False
                    else:
                        color[nei] = color[node] ^ 1
                        stack.append(nei)
                        
        return True
