class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = S.split(' ')
        
        for idx, word in enumerate(s):
            if word[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
                word = word[1:] + word[:1]
            word += 'ma' + ('a' * (idx + 1))
            s[idx] = word
        
        return ' '.join(s)
