class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_to_count = collections.Counter()
        ans = 0
        
        p1 = 0
        for p2 in range(len(s)):
            char_to_count[s[p2]] += 1
            
            while len(char_to_count) > k:
                char_to_count[s[p1]] -= 1
                
                if char_to_count[s[p1]] == 0:
                    char_to_count.pop(s[p1])
                
                p1 += 1
            
            ans = max(ans, p2 - p1 + 1)
        
        return ans
