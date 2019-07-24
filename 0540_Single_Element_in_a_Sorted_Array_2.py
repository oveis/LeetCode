class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        p1, p2 = 0, len(nums)-1
        while p1 < p2:
            mid = (p1 + p2) / 2
            if mid % 2 == 0:
                mid += 1
            
            if nums[mid] == nums[mid-1]:
                p1 = mid + 1
            else:
                p2 = mid - 1
        
        return nums[p1]
