class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        def neighbors(r, c):
            queue = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in queue:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    yield nr, nc
                    
        def dfs_group(r, c, group_id):
            grid[r][c] = group_id
            size = 1
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    size += dfs_group(nr, nc, group_id)
            return size
        
        
        group_id_to_size = {0: 0}
        group_id = 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    group_id_to_size[group_id] = dfs_group(r, c, group_id)
                    group_id += 1
        
        max_size = max(group_id_to_size.values())
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    nei_groups = {grid[nr][nc] for nr, nc in neighbors(r, c)}
                    max_size = max(max_size, 1 + sum([group_id_to_size[group_id] for group_id in nei_groups]))
                    
        return max_size
