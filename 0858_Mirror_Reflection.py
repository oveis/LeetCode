class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m = n = 1
        
        while m * p != n * q:
            n += 1
            m = n * q // p
            
        if m % 2 == 0 and n % 2 == 1:
            return 0
        elif m % 2 == 1 and n % 2 == 0:
            return 2
        elif m % 2 == 1 and n % 2 == 1:
            return 1
        else:
            return -1
