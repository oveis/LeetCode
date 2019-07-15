class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        p1 = p2 = 0
        while p2 < len(nums):
            if p2 + 1 < len(nums) and nums[p2] + 1 == nums[p2 + 1]:
                p2 += 1
            else:
                if p1 == p2:
                    ans.append(str(nums[p1]))
                else:
                    ans.append('{}->{}'.format(nums[p1], nums[p2]))
                p2 += 1
                p1 = p2
        
        return ans
