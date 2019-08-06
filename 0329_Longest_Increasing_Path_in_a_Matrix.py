class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        counter = collections.Counter()
        rows, cols = len(matrix), len(matrix[0])
        
        def dfs(i, j):
            if (i, j) in counter:
                return counter[(i, j)]
            
            cur_val = matrix[i][j]
            
            max_count = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + dx < rows and 0 <= j + dy < cols and \
                    matrix[i + dx][j + dy] > matrix[i][j]:
                    max_count = max(max_count, dfs(i + dx, j + dy))
            
            max_count += 1
            counter[(i, j)] = max_count
            return max_count
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j)
                
        return max(counter.values())
