class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        diff_to_words = collections.defaultdict(list)
        
        for word in strings:
            diffs = []
            for i in range(1, len(word)):
                diff = ord(word[i]) - ord(word[i-1])
                if diff < 0:
                    diff += 26
                diffs.append(diff)
                
            diff_to_words[tuple(diffs)].append(word)
            
        return diff_to_words.values()
