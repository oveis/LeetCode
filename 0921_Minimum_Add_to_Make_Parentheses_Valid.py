class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        count = 0
        left = right = 0
        
        for c in S:
            if c == '(':
                left += 1
            else:
                right += 1
            
            if right > left:
                left += 1
                count += 1
        
        count += (left - right)
        return count
