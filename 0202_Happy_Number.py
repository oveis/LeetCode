class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_set = set()
        while n != 1:
            next_n = 0
            while n > 0:
                next_n += (n % 10) ** 2
                n /= 10
            
            n = next_n
            
            if n in num_set:
                return False
            else:
                num_set.add(n)
                
        return True
