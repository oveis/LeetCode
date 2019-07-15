class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        for pos, c in enumerate(s):
            if c == 'e':
                return self.check_number(s[:pos]) and self.check_number(s[pos+1:], False)
        return self.check_number(s)
    
    
    def check_number(self, s, allow_dot=True):
        if not s:
            return False
        
        pos = 0
        if s[pos] in {'+', '-'}:
            pos += 1
        
        has_num = False
        has_dot = False
        
        while pos < len(s):
            if s[pos].isnumeric():
                has_num = True
            elif allow_dot and not has_dot and s[pos] == '.':
                has_dot = True
            else:
                return False
            pos += 1
        
        return has_num
