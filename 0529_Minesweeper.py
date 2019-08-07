class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        # Clicked 'E'
        self.all_dir = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
        self.dfs(x, y, board)
        return board
        
    
    def dfs(self, x, y, board):
        if board[x][y] != 'E':
            return
        
        mines = self.adjacent_mines(x, y, board)
        
        if mines > 0:
            board[x][y] = str(mines)
        else:
            board[x][y] = 'B'
            for dx, dy in self.all_dir:
                if 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0]):
                    self.dfs(x+dx, y+dy, board)
        
        
    def adjacent_mines(self, x, y, board):
        mines = 0
        for dx, dy in self.all_dir:
            if 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0]) and \
                board[x+dx][y+dy] == 'M':
                mines += 1
        return mines
