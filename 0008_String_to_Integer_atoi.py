class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        
        pos = 0
        while pos < len(str) and str[pos] == ' ':
            pos += 1
        
        sign = 1
        if pos < len(str) and str[pos] in ['+', '-']:
            sign = 1 if str[pos] == '+' else -1
            pos += 1
            
        ans = 0
        for pos in range(pos, len(str)):
            if str[pos].isdigit():
                ans = ans * 10 + int(str[pos])
            else:
                break
        
        ans *= sign
        ans = min(ans, 2**31 -1)
        ans = max(ans, -2**31)
        return ans
