# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    buf4 = []
    
    def read(self, buf: List[str], n: int) -> int:
        buf_idx = 0
        
        while n > 0:
            if len(self.buf4) > 0:
                buf4_size = len(self.buf4)
            else:
                self.buf4 = [''] * 4
                buf4_size = read4(self.buf4)
            
            if buf4_size == 0:
                break
            
            if buf4_size >= n:
                buf[buf_idx: buf_idx + n] = self.buf4[:n]
                self.buf4 = self.buf4[n:]
                buf_idx += n
                break
            else:
                buf[buf_idx: buf_idx + buf4_size] = self.buf4
                self.buf4 = []
                buf_idx += buf4_size
                n -= buf4_size
        
        return buf_idx
