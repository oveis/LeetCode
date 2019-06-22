class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                cmp_c = stack.pop()
                if cmp_c == '(' and c != ')':
                    return False
                elif cmp_c == '{' and c != '}':
                    return False
                elif cmp_c == '[' and c != ']':
                    return False
        
        return len(stack) == 0
