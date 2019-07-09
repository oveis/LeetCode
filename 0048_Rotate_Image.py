class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        last = n - 1
        
        for i in range(n):
            for j in range(i, last-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[last-j][i]
                matrix[last-j][i] = matrix[last-i][last-j]
                matrix[n-i-1][last-j] = matrix[j][last-i]
                matrix[j][last-i] = tmp
