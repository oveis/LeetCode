class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        p_word = p_abbr = 0
        
        while p_word < len(word) and p_abbr < len(abbr):
            if abbr[p_abbr].isalpha() and abbr[p_abbr] == word[p_word]:
                p_abbr += 1
                p_word += 1
            elif abbr[p_abbr].isdigit() and int(abbr[p_abbr]) != 0:
                num = 0
                while p_abbr < len(abbr) and abbr[p_abbr].isdigit():
                    num = num * 10 + int(abbr[p_abbr])
                    p_abbr += 1
                p_word += num
                print(p_word, p_abbr)
            else:
                return False
        
        return p_word == len(word) and p_abbr == len(abbr)
