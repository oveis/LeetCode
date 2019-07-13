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
        
        if i >= 0:
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    self.swap(nums, i, j)
                    break
        
        self.reverse(nums, i)
        
    
    def reverse(self, nums, start):
        p1 = start + 1
        p2 = len(nums) - 1
        while p1 < p2:
            self.swap(nums, p1, p2)
            p1 += 1
            p2 -= 1
    

    def swap(self, nums, p1, p2):
        tmp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = tmp
