from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        nums1_counter = Counter(nums1)
        
        ans = []
        for num in nums2:
            if nums1_counter[num] > 0:
                ans.append(num)
                nums1_counter[num] -= 1
                
        return ans
