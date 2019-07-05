from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_counter = Counter(s)
        
        for idx, c in enumerate(s):
            if s_counter[c] == 1:
                return idx
        
        return -1
