class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_min = -2 ** 31
        int_max = 2**31 -1
        
        is_neg = False
        if x < 0:
            is_neg = True
            x *= -1
        
        rev_x = 0
        while x > 0:
            rev_x *= 10
            rev_x += x % 10
            x /= 10
        
        rev_x *= -1 if is_neg else 1
        
        if rev_x < int_min or rev_x > int_max:
            return 0
        else:
            return rev_x
