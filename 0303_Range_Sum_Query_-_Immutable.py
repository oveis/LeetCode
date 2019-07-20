class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.cumulate_sums = copy.deepcopy(nums)
        for i in range(1, len(nums)):
            self.cumulate_sums[i] += self.cumulate_sums[i-1]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ans = self.cumulate_sums[j]
        if i > 0:
            ans -= self.cumulate_sums[i-1]
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
