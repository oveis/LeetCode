class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        min_flag = True if n < 0 else False
        n = abs(n)
    
        memory_pow = dict()
        ans = self.cal_pow(x, n, memory_pow)
        return 1/ans if min_flag else ans
    
    
    def cal_pow(self, x, n, memory_pow):
        if n == 0:
            ans = 1
        elif n == 1:
            ans = x
        elif n in memory_pow:
            ans = memory_pow[n]
        else:
            ans = self.cal_pow(x, n/2, memory_pow) * self.cal_pow(x, n - n/2, memory_pow)
        
        memory_pow[n] = ans
        return ans
