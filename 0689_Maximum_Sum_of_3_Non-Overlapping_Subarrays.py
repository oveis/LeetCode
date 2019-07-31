class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        W = []
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= k:
                sum_ -= nums[i-k]
            if i >= k-1:
                W.append(sum_)
        
        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W)-1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for p2 in range(k, len(W) - k):
            p1, p3 = left[p2-k], right[p2+k]
            if ans is None or (W[p1] + W[p2] + W[p3] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = p1, p2, p3

        return ans
