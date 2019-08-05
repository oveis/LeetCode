class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        expr = ['(']
        for c in s:
            if c == ' ':
                continue
            elif c.isnumeric():
                if expr and isinstance(expr[-1], int):
                    expr[-1] = expr[-1] * 10 + int(c)
                else:
                    expr.append(int(c))
            else:
                expr.append(c)
        expr.append(')')
        
        _, num = self.evaluate(expr, 1)
        return num
    
    
    def calc(self, opr, num, last):
        if opr == '+':
            return num, num
        elif opr == '-':
            return -num, -num
        elif opr == '*':
            return -last + (last * num), last * num
        else:
            if last < 0:
                new_last = -(-last / num)
            else:
                new_last = last / num
            return -last + new_last, new_last
    
    
    def evaluate(self, expr, i):    
        ans = 0
        opr = '+'
        last = 0
        
        while expr[i] != ')':
            atom = expr[i]
            if isinstance(atom, int):
                cal, last = self.calc(opr, atom, last)
                ans += cal
            elif atom == '(':
                i, num = self.evaluate(expr, i + 1)
                cal, last = self.calc(opr, num, last)
                ans += cal
            else:
                opr = atom
            i += 1
        
        return i, ans
