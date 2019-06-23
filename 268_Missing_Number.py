class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exp_sum = 0
        for i in range(0, len(nums)+1):
            exp_sum += i
        
        for num in nums:
            exp_sum -= num
        
        return exp_sum
