class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_subsets(0, nums, [], result)
        return result

    
    def get_subsets(self, pos, nums, cur_set, result):
        if pos == len(nums):
            result.append(cur_set)
            return
        
        self.get_subsets(pos+1, nums, cur_set, result)
        self.get_subsets(pos+1, nums, cur_set + [nums[pos]], result)
