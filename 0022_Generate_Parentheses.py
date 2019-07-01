class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left_p, right_p = n, n
        results = []
        cur = ''
        self.genRecParen(left_p, right_p, cur, results)
        return results


    def genRecParen(self, left_p, right_p, cur, results):
        if left_p == 0 and right_p == 0:
            results.append(cur)
        elif left_p == right_p:
            self.genRecParen(left_p - 1, right_p, cur + '(', results)
        else:
            if left_p > 0:
                self.genRecParen(left_p - 1, right_p, cur + '(', results)
            self.genRecParen(left_p, right_p - 1, cur + ')', results)
