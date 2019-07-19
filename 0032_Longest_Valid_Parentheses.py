class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        stack = [-1]
        for idx, val in enumerate(s):
            if val == '(':
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    ans = max(ans, idx - stack[-1])
        return ans
