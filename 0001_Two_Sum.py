class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remain_to_idx = dict()
        
        for idx, num in enumerate(nums):
            remain = target - num
            
            if remain in remain_to_idx:
                return [remain_to_idx[remain], idx]
            
            remain_to_idx[num] = idx
        
        return None