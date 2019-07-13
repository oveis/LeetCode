class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        words = [word.strip() for word in s.split(' ')]
        ans = [word for word in words if word]
        return ' '.join(ans[::-1])
