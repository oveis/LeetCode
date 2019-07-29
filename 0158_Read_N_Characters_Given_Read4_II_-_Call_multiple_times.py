"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    remains = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while self.remains and i < n:
            buf[i] = self.remains.pop(0)
            i += 1
        
        while i < n:
            tmp_buf = [''] * 4
            res = read4(tmp_buf)
            while tmp_buf and i < n:
                buf[i] = tmp_buf.pop(0)
                i += 1
            
            if tmp_buf:
                self.remains = tmp_buf
                break
            elif res < 4:
                break
        
        return i
