class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = {'0000'}
        deadends = set(deadends)
        visited = set()
        step = 0
        
        def shift(combo):
            shifts = set()
            for i in range(4):
                for d in [-1, 1]:
                    shifted = (int(combo[i]) + d) % 10
                    shifts.add(combo[:i] + str(shifted) + combo[i+1:])
            return shifts
        
        while queue:
            next_queue = set()
            
            for combo in queue:
                if combo == target:
                    return step
                elif combo in deadends or combo in visited:
                    continue
                
                visited.add(combo)
                next_queue.update(shift(combo))
                
            queue = next_queue
            step += 1
            
        return -1
