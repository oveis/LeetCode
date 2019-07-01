class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        stack_a = []
        for val in a:
            stack_a.append(int(val))
            
        stack_b = []
        for val in b:
            stack_b.append(int(val))
        
        result = ''
        carry = 0
        while stack_a or stack_b:
            carry += stack_a.pop() if stack_a else 0
            carry += stack_b.pop() if stack_b else 0
            
            result = str(carry % 2) + result
            carry /= 2
        
        if carry > 0:
            result = str(carry) + result
            
        return result
