class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        p1 = p2 = 0
        words = []
        
        while p2 < len(s):
            if s[p1] == ' ' and s[p2] != ' ':
                p1 = p2
            elif s[p1] != ' ' and s[p2] == ' ':
                words.append(s[p1:p2])
                p1 = p2
            p2 += 1
        
        if p1 < len(s) and s[p1] != ' ':
            words.append(s[p1:p2])
            
        return ' '.join(words[::-1])
