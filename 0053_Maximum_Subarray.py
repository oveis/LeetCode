class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
#         max_sub = nums[0]
        
#         for p1 in range(len(nums)):
#             cur_sub = 0
            
#             for p2 in range(p1, len(nums)):
#                 cur_sub += nums[p2]
#                 max_sub = max(max_sub, cur_sub)
                
#                 if cur_sub < 0:
#                     break
            
#         return max_sub

        # Solution 2
        max_num = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            
            max_num = max(max_num, nums[i])
        
        return max_num
