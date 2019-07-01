class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        
        self.num_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.result = []
        
        self.gen_strs(digits, '')
        return self.result
        
    
    def gen_strs(self, digits, cur_str):
        if digits == '':
            self.result.append(cur_str)
            return
    
        for c in self.num_dict[digits[0]]:
            self.gen_strs(digits[1:], cur_str + c)
