class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        regex_words = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                regex = word[:i] + '.' + word[i+1:]
                regex_words[regex].append(word)

        queue = [[beginWord]]
        visited = set(beginWord)
        
        while queue:
            new_queue = []
            new_visited = set()
            
            for cur_list in queue:
                last_word = cur_list[-1]

                for i in range(len(last_word)):
                    regex = last_word[:i] + '.' + last_word[i+1:]
                    
                    for next_word in regex_words[regex]:
                        if next_word not in visited:
                            new_queue.append(cur_list + [next_word])
                            new_visited.add(next_word)
            
            ans = [x for x in new_queue if x[-1] == endWord]
            if ans:
                return ans
            
            queue = new_queue
            visited.update(new_visited)
        
        return []
