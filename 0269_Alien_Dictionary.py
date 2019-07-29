class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        char_to_pres = collections.defaultdict(set)
        self.get_pre_chars(words, char_to_pres)
        
        ans = ''
        
        while char_to_pres:
            next_char = None
            
            for char, pres in char_to_pres.items():
                if not pres:
                    next_char = char
                    break
                
            if next_char is None:
                return ''
            
            for char, pres in char_to_pres.items():
                if next_char in pres:
                    pres.remove(next_char)
        
            ans += next_char
            char_to_pres.pop(next_char)
            
        return ans
            
        
    def get_pre_chars(self, words, char_to_pres):
        first_ch = []
        ch_to_words = collections.defaultdict(list)
        
        for word in words:
            if not first_ch or first_ch[-1] != word[0]:
                first_ch.append(word[0])
                
            ch_to_words[word[0]].append(word)
        
        for idx, ch in enumerate(first_ch):
            char_to_pres[ch].update(first_ch[:idx])
        
        for _, ws in ch_to_words.items():
            next_words = [w[1:] for w in ws if w[1:]]
            self.get_pre_chars(next_words, char_to_pres)
