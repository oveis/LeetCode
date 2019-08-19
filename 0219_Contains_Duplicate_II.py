class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_to_pos = collections.defaultdict(int)
        for pos, num in enumerate(nums):
            if num in num_to_pos and pos - num_to_pos[num] <= k:
                return True
            num_to_pos[num] = pos
                
        return False
