class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.left_to_right = 0      # \ diagonal
        self.right_to_left = 0      # / diagonal
        
        
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        score = -1 if player == 1 else 1
        
        self.rows[row] += score
        self.cols[col] += score
        
        if row == col:
            self.left_to_right += score
            
        if row + col + 1 == self.n:
            self.right_to_left += score
        
        expect_sum = score * self.n
        if self.rows[row] == expect_sum or \
            self.cols[col] == expect_sum or \
            self.left_to_right == expect_sum or \
            self.right_to_left == expect_sum:
            
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
