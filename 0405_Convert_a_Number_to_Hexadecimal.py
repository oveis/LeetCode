class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        elif num < 0:
            num = 2 ** 32 + num
        
        ans = ''
        while num > 0:
            n = num % 16
            ans += chr(ord('a') + n - 10) if n >= 10 else str(n)
            num /= 16
        
        return ans[::-1]
