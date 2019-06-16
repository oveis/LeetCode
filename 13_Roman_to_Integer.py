class Solution(object):
    roman_dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for idx, ch in enumerate(s):
            val = self.roman_dic[ch]
            if idx < len(s)-1 and self.roman_dic[s[idx+1]] > val:
                val *= -1
            result += val
        return result
