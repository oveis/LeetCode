class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        p1 = 0
        min_length = float('inf')
        cur_sum = 0
        
        for idx, num in enumerate(nums):
            cur_sum += num
            
            while cur_sum - nums[p1] >= s:
                cur_sum -= nums[p1]
                p1 += 1
                
            if cur_sum >= s:
                min_length = min(min_length, idx - p1 + 1)
                
        return min_length if min_length < float('inf') else 0
