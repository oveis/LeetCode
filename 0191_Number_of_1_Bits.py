class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        weight = 0
        while n > 0:
            weight += n & 1
            n >>= 1
        return weight
