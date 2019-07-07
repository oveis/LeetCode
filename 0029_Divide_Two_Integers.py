class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient, _ = self.minus(dividend, divisor)
        
        if negative:
            quotient *= -1
            
        return max(min(quotient, 2 ** 31 -1), -2 ** 31)
        
    
    def minus(self, dividend, divisor):
        if dividend < divisor:
            return 0, dividend
    
        quotient, reminder = self.minus(dividend, divisor << 1)
        quotient <<= 1
        if reminder >= divisor:
            reminder -= divisor
            quotient += 1
        
        return quotient, reminder
