class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.search_word(i, j, word, board):
                        return True
        
        return False
        
        
    def search_word(self, i, j, word, board):
        if word == '':
            return True
        elif i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] == word[0]:
            cur_ch = board[i][j]
            board[i][j] = ''
            is_found = self.search_word(i-1, j, word[1:], board) or \
                       self.search_word(i+1, j, word[1:], board) or \
                       self.search_word(i, j-1, word[1:], board) or \
                       self.search_word(i, j+1, word[1:], board)
            
            if is_found:
                return True
            else:
                board[i][j] = cur_ch
                return False
        
        return False
