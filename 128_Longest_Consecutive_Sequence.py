class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        num_set = {nums[0]}
        group_list = [(nums[0], nums[0])]
        
        for num in nums[1:]:
            if num in num_set:
                continue
                
            for idx, group in enumerate(group_list):
                if num == group[0] - 1:
                    group_list[idx] = (num, group[1])
                    self.merge_with_next_group(idx-1, group_list)
                    break
                elif num == group[1] + 1:
                    group_list[idx] = (group[0], num)
                    self.merge_with_next_group(idx, group_list)
                    break
                elif num < group[0]:
                    group_list.insert(idx, (num, num))
                    break
                elif idx == len(group_list) - 1:
                    group_list.append((num, num))
                    break
            
            num_set.add(num)
        
        max_len = 0
        for group in group_list:
            max_len = max(max_len, group[1] - group[0] + 1)
        
        return max_len
                
        
    def merge_with_next_group(self, idx, group_list):
        if idx < 0 or idx + 1 >= len(group_list):
            return
        
        group1 = group_list[idx]
        group2 = group_list[idx + 1]
        
        if group1[1] + 1 == group2[0]:
            group_list[idx] = (group1[0], group2[1])
            group_list.pop(idx+1)
