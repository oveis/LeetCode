class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_to_right = copy.deepcopy(nums)
        right_to_left = copy.deepcopy(nums)
        
        for i in range(1, len(nums)):
            left_to_right[i] += left_to_right[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right_to_left[i] += right_to_left[i+1]
            
        for i in range(len(nums)):
            if left_to_right[i] == right_to_left[i]:
                return i
        
        return -1
