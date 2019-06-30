class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        tried_substring = dict()
        return self.wordBreakRec(s, wordDict, tried_substring)
    
    
    def wordBreakRec(self, s, wordDict, tried_substring):
        if (s == '') or (s in wordDict):
            return True
        elif s in tried_substring:
            return tried_substring[s]
    
        for i in range(1, len(s)):
            left_ans = self.wordBreakRec(s[:i], wordDict, tried_substring)
            right_ans = self.wordBreakRec(s[i:], wordDict, tried_substring)
            
            if left_ans and right_ans:
                tried_substring[s] = True
                return True
        
        tried_substring[s] = False
        return False
