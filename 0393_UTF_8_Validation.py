class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            byte = data[i]
            
            n = 0
            bit = 1 << 7
            while bit and (byte & bit):
                n += 1
                bit >>= 1
            
            if n == 0:
                i += 1
                continue
            elif n == 1 or n > 4:
                return False
            
            i += 1
            for _ in range(n-1):
                if i >= len(data) or (128 + 64) & data[i] != 128:
                    return False
                i += 1
                
        return True
