class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        checked_students = set()
        circle_count = 0
        
        for i in range(len(M)):
            if i not in checked_students:
                circle_count += 1
                queue = [i]
                
                while queue:
                    s = queue.pop()
                    checked_students.add(s)
                    
                    for j in range(len(M)):
                        if M[s][j] == 1 and j not in checked_students:
                            queue.append(j)
                            
        return circle_count
