class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        nums.insert(0, lower-1)
        nums.append(upper+1)
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
                ans.append(str(nums[i]-1))
            elif nums[i] - nums[i-1] > 2:
                ans.append('{}->{}'.format(nums[i-1]+1, nums[i]-1))
        return ans
