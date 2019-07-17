class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        cur_sum = 0
        sum_counter = collections.Counter()
        sum_counter[0] = 1
        
        for num in nums:
            cur_sum += num
            
            diff = cur_sum - k
            count += sum_counter.get(diff, 0)
            
            sum_counter[cur_sum] += 1 
        
        return count
