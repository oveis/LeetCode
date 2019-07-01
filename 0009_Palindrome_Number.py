class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tmp_x = x
        rev_x = 0
        
        while tmp_x > 0:
            rev_x *= 10
            rev_x += tmp_x % 10
            tmp_x /= 10
            
        return x == rev_x
