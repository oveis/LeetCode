class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_pos = dict()
        
        for num in nums1:
            num_pos[num] = -1
        
        for idx, num in enumerate(nums2):
            if num in num_pos:
                num_pos[num] = idx
        
        ans = []
        for num in nums1:
            pos = num_pos[num]
            next_greater = -1
            
            for i in range(pos+1, len(nums2)):
                if nums2[i] > num:
                    next_greater = nums2[i]
                    break
            
            ans.append(next_greater)
        
        return ans
