class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        rows = len(rooms)
        cols = len(rooms[0])
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    distance = 0
                    queue = [(i, j)]
                    
                    while queue:
                        next_queue = []
                        
                        for (x, y) in queue:
                            if 0 <= x < rows and 0 <= y < cols and rooms[x][y] >= distance:
                                rooms[x][y] = distance
                                
                                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                    next_queue.append((x + dx, y + dy))
                        
                        queue = next_queue
                        distance += 1
