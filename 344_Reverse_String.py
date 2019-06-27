class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            c = s[p1]
            s[p1] = s[p2]
            s[p2] = c
            p1 += 1
            p2 -= 1
