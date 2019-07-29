# Time Limit Exceeded solution (30 / 72 test cases passed)

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        dist_grids = []
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dist_grids.append(self.make_dist_grid(i, j, grid, rows, cols))
                
        ans = float('inf')
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    total_dist = 0
                    for dist_grid in dist_grids:
                        total_dist += dist_grid[i][j]
                    ans = min(total_dist, ans)
        
        return ans if ans != float('inf') else -1
        
        
    def make_dist_grid(self, i, j, grid, rows, cols):
        dist_grid = [[float('inf')] * cols for _ in range(rows)]
        
        def dfs(i, j, cur_dist):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 0:
                return
            elif dist_grid[i][j] < cur_dist:
                return
            
            dist_grid[i][j] = cur_dist
            dfs(i-1, j, cur_dist + 1)
            dfs(i+1, j, cur_dist + 1)
            dfs(i, j-1, cur_dist + 1)
            dfs(i, j+1, cur_dist + 1)
            
        dfs(i-1, j, 1)
        dfs(i+1, j, 1)
        dfs(i, j-1, 1)
        dfs(i, j+1, 1)
        return dist_grid
        
