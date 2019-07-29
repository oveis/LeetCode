class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        distances = copy.deepcopy(grid)
        house = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                
                house_distance = 1
                queue = [(row, col)]
                
                while queue:
                    next_queue = []
                    
                    for r, c in queue:
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == -house:
                                distances[r + dr][c + dc] += house_distance
                                next_queue.append((r + dr, c + dc))
                                grid[r + dr][c + dc] -= 1
                
                    queue = next_queue
                    house_distance += 1
                
                house += 1
        
        reachable = [distances[r][c] for r in range(rows) for c in range(cols) if grid[r][c] == -house]
        return min(reachable) if reachable else -1
