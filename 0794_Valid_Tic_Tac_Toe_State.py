class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        counts = collections.Counter()
        for i in range(3):
            for j in range(3):
                counts[board[i][j]] += 1
    
        player1_win = self.is_win_by_player(board, 'X')
        player2_win = self.is_win_by_player(board, 'O')
        
        if counts['X'] == counts['O']:
            return player1_win is False
        elif counts['X'] == counts['O'] + 1:
            return player2_win is False
        else:
            return False
        
        
    def is_win_by_player(self, board, player):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == player:
                return True
            
        return board[0][0] == board[1][1] == board[2][2] == player or \
                board[0][2] == board[1][1] == board[2][0] == player
