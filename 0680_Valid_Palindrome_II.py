class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return self.check_palindrome(s[:p1] + s[p1+1:]) or \
                        self.check_palindrome(s[:p2] + s[p2+1:])
        
        return True
    
    
    def check_palindrome(self, s):
        return s == s[::-1]
