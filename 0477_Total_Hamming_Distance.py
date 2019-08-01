class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        while True:
            count_1 = 0
            for i in range(len(nums)):
                count_1 += nums[i] & 1
                nums[i] >>= 1
            
            ans += count_1 * (len(nums) - count_1)
            
            if sum(nums) == 0:
                return ans  
