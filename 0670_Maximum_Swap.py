class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = [int(x) for x in str(num)]
        
        max_seen, max_seen_i = -1, -1
        promote, demote = -1, -1
        
        for i in range(len(s)-1, -1, -1):
            digit = s[i]
            if digit > max_seen:
                max_seen, max_seen_i = digit, i
            elif digit < max_seen:
                promote, demote = max_seen_i, i
                
        if demote == -1:
            return num
        
        s[promote], s[demote] = s[demote], s[promote]
        
        ans = 0
        for n in s:
            ans = ans * 10 + n
        return ans
                
