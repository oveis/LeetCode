class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left_right_mul = [nums[0]]
        for idx in range(1, len(nums)):
            left_right_mul.append(left_right_mul[-1] * nums[idx])
        
        right_left_mul = [nums[-1]]
        for idx in range(len(nums)-2, -1, -1):
            right_left_mul.insert(0, nums[idx] * right_left_mul[0])
        
        output = [right_left_mul[1]]
        
        for i in range(1, len(nums)-1):
            output.append(left_right_mul[i-1] * right_left_mul[i+1])
        
        output.append(left_right_mul[-2])
        return output
