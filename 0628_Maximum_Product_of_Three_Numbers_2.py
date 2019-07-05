class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        
        large_nums = []
        small_nums = []
        
        for num in nums:
            
            insert_idx = len(large_nums)
            for j in range(len(large_nums)):
                if num > large_nums[j]:
                    insert_idx = j
                    break
            
            large_nums.insert(insert_idx, num)
            large_nums = large_nums[:3]
                
            insert_idx = len(small_nums)
            for j in range(len(small_nums)):
                if num < small_nums[j]:
                    insert_idx = j
                    break
            
            small_nums.insert(insert_idx, num)
            small_nums = small_nums[:2]
            
        return max(small_nums[0] * small_nums[1] * large_nums[0],
                      large_nums[0] * large_nums[1] * large_nums[2])
