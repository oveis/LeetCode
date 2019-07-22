class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                regex_word = self.get_regex_word(word, i)
                combo_dict[regex_word].append(word)
        
        visited = set()
        queue = [beginWord]
        level = 1
        
        while queue:
            next_queue = []
            
            for word in queue:
                if word == endWord:
                    return level
                
                visited.add(word)
                
                for i in range(len(word)):
                    regex_word = self.get_regex_word(word, i)
                    
                    for next_word in combo_dict[regex_word]:
                        if next_word not in visited:
                            next_queue.append(next_word)
                
            queue = next_queue
            level += 1
        
        return 0
        
        
    def get_regex_word(self, word, pos):
        return word[:pos] + '?' + word[pos+1:] 
