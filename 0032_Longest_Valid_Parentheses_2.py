class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = right = 0
        
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                ans = max(ans, left + right)
            elif left < right:
                left = right = 0
        
        left = right = 0
        for idx in range(len(s)-1, -1, -1):
            c = s[idx]
            if c == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                ans = max(ans, left + right)
            elif left > right:
                left = right = 0
        
        return ans
