from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_t = Counter(t)
        ans = (float('inf'), 0, 0)
        
        dict_window = {}
        p1, p2 = 0, 0
        
        for p2, char in enumerate(s):
            if char in dict_t:
                dict_window[char] = dict_window.get(char, 0) + 1
                ans, p1 = self.get_min_window(dict_window, dict_t, ans, s, p1, p2)
        
        return s[ans[1]:ans[2]+1] if ans[0] != float('inf') else ''
                
                
    def get_min_window(self, dict_window, dict_t, ans, s, p1, p2):
        while self.has_all_char(dict_window, dict_t):
            window_len = p2 - p1 + 1
            if window_len < ans[0]:
                ans = (window_len, p1, p2)
            
            if s[p1] in dict_window:
                dict_window[s[p1]] -= 1
                
            p1 += 1
        return ans, p1
                
                
    def has_all_char(self, dict_window, dict_t):
        for key, val in dict_t.items():
            if key not in dict_window or dict_window[key] < val:
                return False
        return True
