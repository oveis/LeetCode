class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.get_refined_string(S) == self.get_refined_string(T)
        
    
    def get_refined_string(self, s):
        stack = []
        
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)
