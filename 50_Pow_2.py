class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        N = abs(n)
        
        half = self.myPow(x, N/2)
        if N % 2 == 0:
            ans = half * half
        else:
            ans = half * half * x
        
        return ans if n > 0 else 1/ans
