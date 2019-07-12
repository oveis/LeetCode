class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.backtrack(0, board)
                
    
    def backtrack(self, pos, board):
        for p in range(pos, 9*9):
            i, j = p / 9, p % 9
            
            if board[i][j] == '.':
                candidates = [True] * 9
                self.check_row(i, j, board, candidates)
                self.check_col(i, j, board, candidates)
                self.check_subbox(i, j, board, candidates)

                for idx, val in enumerate(candidates):
                    if val:
                        board[i][j] = str(idx + 1)
                        if self.backtrack(p + 1, board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
        return True
        
    
    def check_row(self, i, j, board, candidates):
        for col in range(len(board[0])):
            digit = board[i][col]
            if digit != '.':
                candidates[int(digit) - 1] = False
                
                
    def check_col(self, i, j, board, candidates):
        for row in range(len(board)):
            digit = board[row][j]
            if digit != '.':
                candidates[int(digit) - 1] = False
                
    
    def check_subbox(self, i, j, board, candidates):
        for row in range(i/3*3, (i/3+1)*3):
            for col in range(j/3*3, (j/3+1)*3):
                digit = board[row][col]
                if digit != '.':
                    candidates[int(digit) - 1] = False
