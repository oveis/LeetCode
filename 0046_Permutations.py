class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.get_permute([], nums, ans)
        return ans
    
    
    def get_permute(self, cur, nums, ans):
        if not nums:
            ans.append(cur)
            return
    
        for idx, num in enumerate(nums):
            self.get_permute(cur + [num], nums[:idx] + nums[idx+1:], ans)
