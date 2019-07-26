class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        i = 1
        while i ** 2 <= n:
            ans += 1
            i += 1
        return ans
