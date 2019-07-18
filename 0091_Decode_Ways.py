class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0] * len(s)
        digit_set = set()
        for d in range(1, 27):
            digit_set.add(str(d))
        
        for i in range(len(s)):
            if s[i] in digit_set:
                counts[i] = counts[i-1] if i >= 1 else 1
            
            if i >= 1 and (s[i-1] + s[i]) in digit_set:
                counts[i] += counts[i-2] if i >= 2 else 1
            
            if counts[i] == 0:
                break
        
        return counts[-1]
