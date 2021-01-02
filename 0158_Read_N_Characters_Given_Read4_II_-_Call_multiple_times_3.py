# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = deque([])
        
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.pop(0)
                i += 1
            else:
                buf4 = [''] * 4
                buf4_size = read4(buf4)
                
                if buf4_size == 0:
                    break
                
                self.q = buf4
                
        return i
