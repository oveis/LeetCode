class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = 0
        num_pos = None
        
        for p1, val in enumerate(s):    
            if val >= '0' and val <= '9':
                num = num * 10 + int(val)
                if num_pos == None:
                    num_pos = p1
            elif val == '[':
                left, right = 1, 0
                
                for p2 in range(p1+1, len(s)):
                    if s[p2] == '[':
                        left += 1
                    elif s[p2] == ']':
                        right += 1
                    if left == right:
                        break
                
                new_s = s[:num_pos]
                new_s += self.decodeString(num * s[p1+1:p2])
                new_s += self.decodeString(s[p2+1:])
                return new_s
        
        return s
