class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for idx in range(len(digits)-1, -1, -1):
            carry += digits[idx]
            digits[idx] = carry % 10
            carry /= 10
        
        if carry > 0:
            digits.insert(0, carry)
        
        return digits
