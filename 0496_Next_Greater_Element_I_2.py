class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        num_greater = dict()
        
        for num in nums2:
            while stack and num > stack[-1]:
                num_greater[stack.pop()] = num
                
            stack.append(num)
            
        while stack:
            num_greater[stack.pop()] = -1
            
        ans = []
        for num in nums1:
            ans.append(num_greater[num])
        
        return ans
