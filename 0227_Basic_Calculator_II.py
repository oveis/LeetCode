class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        expr = []
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
        
        num = 0
        opr = '+'
        last = 0
        
        for x in expr:
            if isinstance(x, int):
                if opr == '+':
                    num += x
                    last = x
                elif opr == '-':
                    num -= x
                    last = -x
                elif opr == '*':
                    num = num - last + (last * x)
                    last = last * x
                else:
                    sign = 1
                    if last < 0:
                        sign = -1
                        last *= -1
                    num = num - sign * last + sign * (last / x)
                    last = sign * (last / x)
            else:
                opr = x
                
        return num
