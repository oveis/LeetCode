class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums)-1
        
        while p1 < p2:
            mid = (p1 + p2) / 2
            
            if nums[mid] < nums[p2]:
                p2 = mid
            else:
                p1 = mid + 1
        
        return nums[p1]
