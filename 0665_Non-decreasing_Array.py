class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                return self.check_non_decreasing(nums[:i] + nums[i+1:]) or \
                        self.check_non_decreasing(nums[:i+1] + nums[i+2:])
        return True
        
        
    def check_non_decreasing(self, nums):
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                return False
        return True
