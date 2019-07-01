class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest_len = 0
        
        for num in num_set:
            
            # Only search when there is no consecutive lower number of this.
            if num -1 not in num_set:
                cur_num = num
                cur_len = 1

                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_len += 1

                longest_len = max(longest_len, cur_len)
        
        return longest_len
