class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alpha_order = {' ': 0}
        for idx, alpha in enumerate(order):
            alpha_order[alpha] = idx + 1
        
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            
            while word1 and word2:
                if word1[0] == word2[0]:
                    word1 = word1[1:]
                    word2 = word2[1:]
                else:
                    break

            word1 = ' ' if word1 == '' else word1
            word2 = ' ' if word2 == '' else word2
            
            if alpha_order[word1[0]] > alpha_order[word2[0]]:
                return False
        
        return True
