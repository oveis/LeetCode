class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_s = str(num)
        conv_s = ''
        
        for c in num_s:
            if c not in ['0', '1', '6', '8', '9']:
                return False
            
            if c == '6':
                conv_s += '9'
            elif c == '9':
                conv_s += '6'
            else:
                conv_s += c
            
        return num_s == conv_s[::-1]
