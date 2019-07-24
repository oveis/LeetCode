class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_pos = collections.defaultdict(list)
        remainder_pos[0].append(-1)
        cur_sum = 0
        
        for i, num in enumerate(nums):
            cur_sum += num
            if k != 0:
                cur_sum %= k
            
            if cur_sum in remainder_pos:
                if i - remainder_pos[cur_sum][0] >= 2:
                    return True
            remainder_pos[cur_sum].append(i)
        
        return False
