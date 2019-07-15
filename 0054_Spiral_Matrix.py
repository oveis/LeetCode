class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        
        while matrix:
            ans += matrix.pop(0)
            
            for row in matrix:
                if row:
                    ans.append(row.pop())
            
            if matrix:
                ans += matrix.pop()[::-1]
            
            for row in reversed(matrix):
                if row:
                    ans.append(row.pop(0))
        
        return ans
