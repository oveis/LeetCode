class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        elif len(buildings) == 1:
            (l, r, h) = buildings[0]
            return [[l, h], [r, 0]]
        
        mid = len(buildings) / 2
        left_skyline = self.getSkyline(buildings[:mid])
        right_skyline = self.getSkyline(buildings[mid:])
        
        return self.merge_skylines(left_skyline, right_skyline)
    
    
    def merge_skylines(self, left, right):
        p_left = p_right = 0
        left_height = right_height = cur_height = 0
        output = []
        
        while p_left < len(left) and p_right < len(right):
            if left[p_left][0] < right[p_right][0]:
                x, left_height = left[p_left]
                p_left += 1
            else:
                x, right_height = right[p_right]
                p_right += 1
                
            max_height = max(left_height, right_height)
            
            if cur_height != max_height:
                self.append_output(x, max_height, output)
                cur_height = max_height
    
        self.append_skyline(p_left, left, cur_height, output)
        self.append_skyline(p_right, right, cur_height, output)
            
        return output
    
    
    def append_skyline(self, p, skylines, cur_height, output):
        for p in range(p, len(skylines)):
            x, height = skylines[p]
            if cur_height != height:
                self.append_output(x, height, output)
                cur_height = height
                
    
    def append_output(self, x, height, output):
        if len(output) > 0 and output[-1][0] == x:
            output[-1][1] = height
        else:
            output.append([x, height])
