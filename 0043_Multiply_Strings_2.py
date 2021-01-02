class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        mul_arr = []
        for pos, digit in enumerate(num2[::-1]):
            mul_arr.append(self.multiply_by_digit(num1 + ('0' * pos), digit))
            
        max_len = len(mul_arr[-1])
        ans = []
        carry = 0
        
        for p in range(max_len):
            for arr in mul_arr:
                if p < len(arr):
                    carry += arr[p]
            
            ans.append(str(carry % 10))
            carry //= 10
            
        if carry > 0:
            ans.append(str(carry))
            
        return ''.join(ans[::-1])
        
        
    
    def multiply_by_digit(self, num: str, digit: str) -> List[int]:
        ans = []
        carry = 0
        for n in num[::-1]:
            carry = int(n) * int(digit) + carry
            ans.append(carry % 10)
            carry //= 10
        
        if carry > 0:
            ans.append(carry)
            
        return ans
