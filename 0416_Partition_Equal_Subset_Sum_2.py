class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total / 2
        
        subset_sum = [True] + [False] * target
        for num in nums:
            for i in range(target - 1, -1, -1):
                if subset_sum[i] and i + num <= target:
                    if i + num == target:
                        return True
                    subset_sum[i + num] = True
        return False
