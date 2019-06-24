class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.sink_island(i, j, grid)
        
        return count
    
    
    def sink_island(self, row, col, grid):
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == '1':
            grid[row][col] = '0'
            self.sink_island(row-1, col, grid)
            self.sink_island(row+1, col, grid)
            self.sink_island(row, col-1, grid)
            self.sink_island(row, col+1, grid)
