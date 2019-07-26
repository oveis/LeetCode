from collections import defaultdict

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_count = defaultdict(int)
        sum_count[0] = 1
        
        for num in nums:
            next_sum_count = defaultdict(int)
            
            for s, count in sum_count.items():
                next_sum_count[s + num] += count
                next_sum_count[s - num] += count
                
            sum_count = next_sum_count
        
        return sum_count[S]
