class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.get_refined_string(S) == self.get_refined_string(T)
        
    
    def get_refined_string(self, s):
        pos = 0
        
        while pos < len(s):
            if s[pos] == '#':
                if pos == 0:
                    s = s[pos+1:]
                else:
                    s = s[:pos-1] + s[pos+1:]
                    pos -= 1
            else:
                pos += 1
        
        return s
