class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        minus = False
        if numerator * denominator < 0:
            minus = True
        numerator, denominator = abs(numerator), abs(denominator)
            
        quotient = numerator / denominator
        remainder = numerator % denominator
        
        fraction = []
        remainder_pos_dict = dict()
        while remainder > 0:
            remainder *= 10
            if remainder in remainder_pos_dict:
                fraction.insert(remainder_pos_dict[remainder], '(')
                fraction.append(')')
                break
            elif remainder / denominator > 0:
                remainder_pos_dict[remainder] = len(fraction)
                fraction.append(str(remainder / denominator))
                remainder %= denominator
            else:
                fraction.append('0')
        
        ans = ('-' if minus else '') + str(quotient)
        if fraction:
            ans += '.' + ''.join(fraction)
            
        return ans
