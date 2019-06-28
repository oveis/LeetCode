class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = set()
        self.gen_valid_par(0, 0, s, '', output)
        output = list(output)
        print('[output] {}'.format(output))
        
        for length in range(len(s), -1, -1):
            result = [val for val in output if len(val) == length]
            if len(result) > 0:
                return result
            
        return [s]

    
    def gen_valid_par(self, left, right, s, cur_str, output):
        if s == '':
            if left == right:
                output.add(cur_str)
            return
        elif left < right:
            return
        
        if s[0] == '(':
            self.gen_valid_par(left, right, s[1:], cur_str, output)
            self.gen_valid_par(left + 1, right, s[1:], cur_str + s[0], output)
        elif s[0] == ')':
            self.gen_valid_par(left, right + 1, s[1:], cur_str + s[0], output)
            self.gen_valid_par(left, right, s[1:], cur_str, output)
        else:
            self.gen_valid_par(left, right, s[1:], cur_str + s[0], output)
