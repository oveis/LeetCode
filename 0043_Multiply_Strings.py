class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = ''
        
        for i in range(len(num1)):
            tmp = self.mul_nums(num2, num1[i], i)
            result = self.add_nums(tmp, result)
        
        return result[::-1]

    
    def mul_nums(self, num, digit, zero_trails):
        result = ''
        
        carry = 0
        for i in range(len(num)):
            n = int(digit) * int(num[i]) + carry
            result += str(n % 10)
            carry = n / 10
        
        if carry > 0:
            result += str(carry)
        
        return ('0' * zero_trails) + result
        
    
    def add_nums(self, num1, num2):
        carry = 0
        p1, p2 = 0, 0
        result = ''
        
        while p1 < len(num1) or p2 < len(num2):
            if p1 < len(num1):
                carry += int(num1[p1])
                p1 += 1
            
            if p2 < len(num2):
                carry += int(num2[p2])
                p2 += 1
                
            result += str(carry % 10)
            carry /= 10
        
        if carry > 0:
            result += str(carry)
        
        return result
