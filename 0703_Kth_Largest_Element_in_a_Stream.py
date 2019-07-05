class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.stack = sorted(nums, reverse=True)[:k]
            

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.stack.append(val)
        self.stack = sorted(self.stack, reverse=True)[:self.k]
        return self.stack[-1]
    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
