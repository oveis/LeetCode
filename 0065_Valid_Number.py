class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        
        pos = 0
        if s[pos] in {'+', '-'}:
            pos += 1
        
        has_num = False
        has_dot = False
        has_e = False
        
        while pos < len(s):
            if s[pos].isnumeric():
                has_num = True
                pos += 1
            elif s[pos] == '.':
                if has_dot:
                    return False
                else:
                    has_dot = True
                    pos += 1
            elif s[pos] == 'e':
                has_e = True
                if not has_num:
                    return False
                else:
                    pos += 1
                    break
            else:
                return False
        
        if has_e:
            has_post_num = False
            if pos < len(s) and s[pos] in {'+', '-'}:
                pos += 1

            while pos < len(s):
                if s[pos].isnumeric():
                    has_post_num = True
                    pos += 1
                else:
                    return False
        
            return has_post_num
        else:
            return has_num
