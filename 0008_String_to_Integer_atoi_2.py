class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        ans = 0
        
        sign = 1
        if s and s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        for c in s:
            if not c.isnumeric():
                break
                
            ans = ans * 10 + int(c)
                
        ans *= sign
        
        ans = max(-2 ** 31, ans)
        ans = min(2 ** 31 - 1, ans)
        return ans
