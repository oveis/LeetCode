class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_lp = ''
        
        for p1 in range(0, len(s)):
            max_lp = self.getLongestPalindrome(p1, p1, s, max_lp)
            
            if p1 + 1 < len(s):
                max_lp = self.getLongestPalindrome(p1, p1+1, s, max_lp)
            
        return max_lp
    
    
    def getLongestPalindrome(self, p1, p2, s, max_lp):
        lp = ''
        while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
            lp = s[p1: p2+1]
            p1 -= 1
            p2 += 1
        
        return lp if len(lp) > len(max_lp) else max_lp
