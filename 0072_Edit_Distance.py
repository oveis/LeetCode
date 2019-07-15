class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        if m * n == 0:
            return m + n
        
        board = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            board[i][0] = i
        for i in range(n + 1):
            board[0][i] = i
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = board[i][j-1] + 1
                up = board[i-1][j] + 1
                left_up = board[i-1][j-1] + (0 if word1[i - 1] == word2[j - 1] else 1)
                board[i][j] = min(left, up, left_up)
        
        return board[-1][-1]
