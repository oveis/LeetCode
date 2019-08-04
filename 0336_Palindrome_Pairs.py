class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_to_idx = dict()
        for idx, word in enumerate(words):
            word_to_idx[word] = idx
            
        ans = set()
        for idx, word in enumerate(words):
            
            for i in range(len(word) + 1):
                left, right = word[:i], word[i:]
                rev_left, rev_right = left[::-1], right[::-1]
                
                if right == rev_right and rev_left in word_to_idx:
                    ans.add((idx, word_to_idx[rev_left]))
                
                if left == rev_left and rev_right in word_to_idx:
                    ans.add((word_to_idx[rev_right], idx))
        
        return [(x, y) for x, y in ans if x != y]
