class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permute_set = set()
        self.get_permute([], nums, permute_set)
        return [x.split(',') for x in permute_set]
        
    
    def get_permute(self, cur, nums, permute_set):
        if not nums:
            permute_set.add(','.join([str(x) for x in cur]))
            return
        
        for idx, num in enumerate(nums):
            self.get_permute(cur + [num], nums[:idx] + nums[idx+1:], permute_set)
