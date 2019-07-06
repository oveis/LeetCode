class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        end_k_nums = nums[-k:]
        for i in range(len(nums)-1-k, -1, -1):
            nums[i+k] = nums[i]
        
        for i in range(k):
            nums[i] = end_k_nums[i]
