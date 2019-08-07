class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def traverse(i, j, reverse):
            lst = []
            while i >= 0 and j < len(matrix[0]):
                lst.append(matrix[i][j])
                i, j = i-1, j+1
            
            if reverse:
                lst.reverse()
            return lst
        
        if not matrix:
            return []
        
        ans = []
        reverse = False
        for i in range(len(matrix)):
            ans += traverse(i, 0, reverse)
            reverse = not reverse
            
        for j in range(1, len(matrix[0])):
            ans += traverse(len(matrix) - 1, j, reverse)
            reverse = not reverse
            
        return ans
