class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        w_pos = 0
        for idx, val in enumerate(nums):
            if val != 0:
                tmp = nums[w_pos]
                nums[w_pos] = val
                nums[idx] = tmp
                w_pos += 1
