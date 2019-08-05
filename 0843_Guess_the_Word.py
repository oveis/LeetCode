# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        
        matches = 0
        while matches < 6:
            guess_word = self.get_guess_word(wordlist)
            matches = master.guess(guess_word)
            wordlist = self.get_wordlist(guess_word, matches, wordlist)
            
            
    def get_guess_word(self, wordlist):
        counts = [collections.Counter()] * 6
        for word in wordlist:
            for i, c in enumerate(word):
                counts[i][c] += 1
        
        return max(wordlist, key=lambda x: sum(counts[i][c] for i, c in enumerate(x)))
    
    
    def get_wordlist(self, word, matches, wordlist):
        def count_overlap(a, b):
            return sum(x == y for x, y in zip(a, b))
        
        return [x for x in wordlist if count_overlap(word, x) == matches and x != word]
