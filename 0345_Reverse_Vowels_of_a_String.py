class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        p1, p2 = 0, len(s)-1
        
        while p1 < p2:
            if self.is_vowel(s[p1]) and self.is_vowel(s[p2]):
                tmp = s[p1]
                s[p1] = s[p2]
                s[p2] = tmp
                p1 += 1
                p2 -= 1
            else:
                if not self.is_vowel(s[p1]):
                    p1 += 1    
                if not self.is_vowel(s[p2]):
                    p2 -= 1
            
        return ''.join(s)
                
    
    def is_vowel(self, ch):
        return ch.lower() in ['a', 'e', 'i', 'o', 'u']
