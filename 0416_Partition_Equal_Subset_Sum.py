class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums) / 2.0
        sum_subset = {0}
        for num in nums:
            sum_subset.update({num + x for x in sum_subset})
            if target in sum_subset:
                return True
        return False
