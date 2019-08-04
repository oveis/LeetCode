class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        expr = ['(']
        
        for i, c in enumerate(s):
            if c == ' ':
                continue
            elif c.isnumeric():
                if isinstance(expr[-1], int):
                    expr[-1] = expr[-1] * 10 + int(c)
                else:
                    expr.append(int(c))
            else:
                expr.append(c)
                
        expr.append(')')
        _, num = self.evaluate(expr, 1)
        return num
    
    
    def evaluate(self, expr, i):
        ans = 0
        opr = 1
        
        while expr[i] != ')':
            atom = expr[i]
            
            if isinstance(atom, int):
                ans += opr * atom
            elif atom in ['+', '-']:
                opr = 1 if atom == '+' else -1
            else:
                i, num = self.evaluate(expr, i + 1)
                ans += opr * num
            
            i += 1
        
        return i, ans
