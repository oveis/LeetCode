class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count += self.count_palindrom_sub(i, i, s)
            if i > 0:
                count += self.count_palindrom_sub(i-1, i, s)
        return count
    
    
    def count_palindrom_sub(self, p1, p2, s):
        count = 0
        while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
            p1 -= 1
            p2 += 1
            count += 1
        return count
