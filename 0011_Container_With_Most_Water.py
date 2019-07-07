class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(height)-1
        max_water = 0
        
        while p1 < p2:
            cur_water = (p2 - p1) * min(height[p1], height[p2])
            max_water = max(max_water, cur_water)
            
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        
        return max_water
