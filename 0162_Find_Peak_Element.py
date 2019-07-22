class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums)-1
        
        while p1 < p2:
            mid = (p1 + p2) / 2
            
            if nums[mid] < nums[mid+1]:
                p1 = mid + 1
            else:
                p2 = mid
        
        return p1
