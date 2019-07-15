class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = self.get_target_range(0, len(nums)-1, nums, target)
        return [start, end]
    
    
    def get_target_range(self, p1, p2, nums, target):
        if p1 > p2:
            return (-1, -1)
        elif p1 == p2:
            return (p1, p1) if nums[p1] == target else (-1, -1)
        
        mid = (p1 + p2) / 2
        
        if nums[mid] < target:
            return self.get_target_range(mid+1, p2, nums, target)
        elif nums[mid] > target:
            return self.get_target_range(p1, mid-1, nums, target)
        else:
            left, _ = self.get_target_range(p1, mid-1, nums, target)
            _, right = self.get_target_range(mid+1, p2, nums, target)
            
            left = mid if left == -1 else left
            right = mid if right == -1 else right
            return (left, right)
