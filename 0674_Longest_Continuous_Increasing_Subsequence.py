class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1 = p2 = 0
        lcis = 0
        
        for p2 in range(len(nums)):
            lcis = max(lcis, p2 - p1 + 1)
            
            if p2 + 1 < len(nums) and nums[p2] >= nums[p2+1]:
                p1 = p2 + 1
            
        return lcis
