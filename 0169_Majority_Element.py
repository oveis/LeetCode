from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        
        for num in nums:
            if nums_counter[num] > len(nums)/2:
                return num

        return None
