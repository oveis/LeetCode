class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = set()
        
        for p1 in range(0, len(nums)-2):
            p2 = p1 + 1
            p3 = len(nums) - 1
            
            while p2 < p3:
                s = nums[p1] + nums[p2] + nums[p3]
                
                if s == 0:
                    results.add((nums[p1], nums[p2], nums[p3]))
                    p2 += 1
                    p3 -= 1
                elif s < 0:
                    p2 += 1
                else:
                    p3 -= 1
        
        return [[n1, n2, n3] for (n1, n2, n3) in results]
