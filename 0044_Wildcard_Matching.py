class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        rows = len(p) + 1
        cols = len(s) + 1
        board = [[False] * cols for _ in range(rows)]
        board[0][0] = True
        
        for i in range(1, rows):
            board[i][0] = True if board[i-1][0] and p[i-1] == '*' else False
        
        for j in range(1, cols):
            board[0][j] = False
        
        for i in range(1, rows):
            for j in range(1, cols):
                if p[i-1] == '*':
                    board[i][j] = board[i-1][j] or board[i][j-1] or board[i-1][j-1]
                elif p[i-1] == '?' or p[i-1] == s[j-1]:
                    board[i][j] = board[i-1][j-1]
        
        return board[-1][-1]
