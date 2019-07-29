class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len_to_words = collections.defaultdict(set)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.len_to_words[len(word)].add(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        for w in self.len_to_words[len(word)]:
            for pos, ch in enumerate(w):
                if word[pos] != '.' and word[pos] != ch:
                    break
            else:
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
