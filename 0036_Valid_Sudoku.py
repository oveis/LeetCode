class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.check_rows(board) and \
                self.check_cols(board) and \
                self.check_cells(board)
    
    
    def check_rows(self, board):
        for i in range(9):
            count = collections.Counter()
            for j in range(9):
                count[board[i][j]] += 1
                
            if not self.validate(count):
                return False
            
        return True
    
    
    def check_cols(self, board):
        for j in range(9):
            count = collections.Counter()
            for i in range(9):
                count[board[i][j]] += 1
                
            if not self.validate(count):
                return False
        
        return True
    
    
    def check_cells(self, board):
        for i in range(3):
            for j in range(3):
                count = collections.Counter()
                
                for r in range(i*3, i*3+3):
                    for c in range(j*3, j*3+3):
                        count[board[r][c]] += 1
                
                if not self.validate(count):
                    return False
        
        return True
    
    
    def validate(self, count):
        for i in range(1, 10):
            if count[str(i)] > 1:
                return False
        return True
