class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        refined_s = ''
        for c in s:
            if c.isalnum():
                refined_s += c.lower()
        
        return refined_s == refined_s[::-1]
