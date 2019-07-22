class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        while i < len(s) and i < len(t):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or \
                      s[i:] == t[i+1:] or \
                      s[i+1:] == t[i:]
            i += 1
            
        return abs(len(s) - i + len(t) - i) == 1
