class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        pos1 = len(num1) - 1
        pos2 = len(num2) - 1
        
        ans = ''
        carry = 0
        
        while pos1 >= 0 or pos2 >= 0:
            if pos1 >= 0:
                carry += int(num1[pos1])
                pos1 -= 1
                
            if pos2 >= 0:
                carry += int(num2[pos2])
                pos2 -= 1
        
            ans = str(carry % 10) + ans
            carry /= 10
        
        if carry > 0:
            ans = str(carry) + ans
        
        return ans
