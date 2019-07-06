class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        
        left_sum = 0
        for idx, num in enumerate(nums):
            if left_sum == (s - left_sum - num):
                return idx
            left_sum += num
        
        return -1
