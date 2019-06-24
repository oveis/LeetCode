class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_inters = sorted(intervals, key=lambda interval: interval[0])
        cur_pos = 0
        
        while cur_pos < len(sorted_inters):
            cur_inter = sorted_inters[cur_pos]
            next_pos = cur_pos + 1
            
            if next_pos < len(sorted_inters):
                next_inter = sorted_inters[next_pos]
                
                if next_inter[0] >= cur_inter[0] and next_inter[0] <= cur_inter[1]:
                    cur_inter[1] = max(cur_inter[1], next_inter[1])
                    sorted_inters.pop(next_pos)
                    cur_pos -= 1    # To keep the current position.
            
            cur_pos += 1
        
        return sorted_inters
