class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = hi = 0
        for c in s:
            if c == '(':
                hi += 1
                lo += 1
            elif c == ')':
                hi -= 1
                lo = max(0, lo - 1)
            else:
                hi += 1
                lo = max(0, lo - 1)
        
            if hi < 0:
                return False
        return lo == 0
