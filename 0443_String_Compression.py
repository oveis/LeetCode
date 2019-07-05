class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        
        read_p = write_p = 0
        
        char = chars[0]
        count = 0
        
        while read_p < len(chars):
            if chars[read_p] == char:
                count += 1
            else:
                write_p = self.put_char_count(char, count, chars, write_p)
                char = chars[read_p]
                count = 1        
            read_p += 1
        
        return self.put_char_count(char, count, chars, write_p)
    
    
    def put_char_count(self, char, count, chars, write_p):
        chars[write_p] = char
        write_p += 1
        
        if count > 1:
            count = str(count)
            while count:
                chars[write_p] = count[0]
                count = count[1:]
                write_p += 1
            
        return write_p
