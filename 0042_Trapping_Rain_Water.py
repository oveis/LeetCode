class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_to_right = self.get_dir_height(height)
        right_to_left = self.get_dir_height(reversed(height))
        right_to_left.reverse()
        
        water = 0
        for idx in range(1, len(height)-1):
            diff = min(left_to_right[idx-1], right_to_left[idx+1]) - height[idx]
            water += max(diff, 0)
        return water
        
    
    def get_dir_height(self, height):
        height_list = []
        for idx, h in enumerate(height):
            if idx == 0:
                height_list.append(h)
            else:
                height_list.append(max(height_list[-1], h))
        return height_list
