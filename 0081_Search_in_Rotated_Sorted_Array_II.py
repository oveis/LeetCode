class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        p1, p2 = 0, len(nums)-1
        
        return self.search_helper(nums, target, p1, p2)
        
    
    def search_helper(self, nums, target, p1, p2):
        if p1 > p2:
            return False
        
        mid = (p1 + p2) / 2
        if nums[mid] == target:
            return True
        
        if nums[p1] < nums[mid]:
            if nums[p1] <= target < nums[mid]:
                return self.search_helper(nums, target, p1, mid - 1)
            else:
                return self.search_helper(nums, target, mid + 1, p2)
        elif nums[p1] > nums[mid]:
            if nums[mid] < target <= nums[p2]:
                return self.search_helper(nums, target, mid + 1, p2)
            else:
                return self.search_helper(nums, target, p1, mid - 1)
        elif nums[p1] == nums[mid]:
            if nums[p2] != nums[mid]:
                return self.search_helper(nums, target, mid + 1, p2)
            else:
                return self.search_helper(nums, target, p1, mid - 1) or \
                        self.search_helper(nums, target, mid + 1, p2)
        
        return False
