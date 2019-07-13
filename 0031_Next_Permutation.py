class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) -2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        
        for j, num in enumerate(sorted(nums[i+1:])):
            nums[i+j+1] = num
            
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                break
