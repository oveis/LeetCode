class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos_dict = dict()
        p1, p2 = 0, 0
        
        ll = 0
        while p2 < len(s):
            c_p2 = s[p2]
            
            if c_p2 in pos_dict:
                target_p = pos_dict[c_p2]
                
                while p1 <= target_p:
                    pos_dict.pop(s[p1])
                    p1 += 1
                
            pos_dict[c_p2] = p2
            ll = max(ll, p2 - p1 + 1)
            p2 += 1
        
        return ll
