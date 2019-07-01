class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        cumulate_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(rows):
            for col in range(cols-1, -1, -1):
                if matrix[row][col] != '0':
                    cumulate_matrix[row][col] = cumulate_matrix[row][col+1] + 1 if col < cols-1 else 1
        
        max_area = 0
        
        for row in range(rows):
            for col in range(cols):
                width = cumulate_matrix[row][col]
                for t in range(row, rows):
                    if cumulate_matrix[t][col] == 0:
                        break
                        
                    width = min(width, cumulate_matrix[t][col])
                    max_area = max(max_area, (t - row + 1) * width)
                
        return max_area
