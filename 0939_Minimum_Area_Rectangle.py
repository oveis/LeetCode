class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        columns = collections.defaultdict(list)
        for (x, y) in points:
            columns[x].append(y)
        
        min_area = float('inf')
        lastx = dict()
        
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            
            for i, y2 in enumerate(column):
                for j in range(i):
                    y1 = column[j]
                    
                    if (y1, y2) in lastx:
                        min_area = min(min_area, (y2 - y1) * (x - lastx[(y1, y2)]))
                    
                    lastx[y1, y2] = x
                    
        return min_area if min_area != float('inf') else 0
