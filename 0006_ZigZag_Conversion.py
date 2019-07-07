class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        idx = 0
        direction = -1 
        
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows - 1:
                direction *= -1
        
            idx += direction
        
        return ''.join(rows)
