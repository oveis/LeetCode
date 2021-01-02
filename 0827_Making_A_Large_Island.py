class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        nei_count_grid = self.get_nei_count_grid(grid)
        max_size = 0
        found_island = False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if nei_count_grid[i][j] >= 1:
                    found_island = True
                    grid[i][j] = 1
                    island_size = self.cal_island_size(grid, i, j)
                    max_size = max(max_size, island_size)
                    grid[i][j] = 0
                    
        if found_island:
            return max_size
        else:
            return 1 if grid[0][0] == 0 else len(grid) * len(grid[0])
                    
                    
    def get_nei_count_grid(self, grid: List[List[int]]) -> List[List[int]]:
        count_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count_grid[i][j] = self.get_nei_count(grid, i, j)
                    
        return count_grid
                    
                    
    def get_nei_count(self, grid, i, j):
        count = 0
        count += grid[i-1][j] if i > 0 else 0
        count += grid[i][j-1] if j > 0 else 0
        count += grid[i+1][j] if i < len(grid) - 1 else 0
        count += grid[i][j+1] if j < len(grid[0]) - 1 else 0
        return count
        
    
    def cal_island_size(self, grid: List[List[int]], row: int, col: int) -> int:
        island_size = 0
        visited = set()
        queue = [(row, col)]
        
        while queue:
            (i, j) = queue.pop()
            if (i, j) in visited or \
                not (0 <= i < len(grid)) or \
                not (0 <= j < len(grid[0])) or \
                grid[i][j] == 0:
                continue
            
            visited.add((i, j))
            island_size += 1
            
            queue += [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            
        return island_size
                
