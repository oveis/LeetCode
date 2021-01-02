class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = right = 0
        
        idx = 0
        while idx < len(s):
            if s[idx] == '(':
                left += 1
            elif s[idx] == ')':
                if left < right + 1:
                    s = s[:idx] + s[idx+1:]
                    continue
                right += 1
            idx += 1
            
        left_surplus_count = left - right
        idx = len(s) - 1
        
        while idx >= 0 and left_surplus_count > 0:
            if s[idx] == '(':
                s = s[:idx] + s[idx+1:]
                left_surplus_count -= 1
            idx -= 1
                
        return s
