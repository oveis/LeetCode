class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0] * m for _ in range(n)]
        grid[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                grid[i][j] += grid[i-1][j] if i > 0 else 0
                grid[i][j] += grid[i][j-1] if j > 0 else 0
        
        return grid[-1][-1]
