class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        self.put_queen([], n, ans)
        return ans
    
        
    def put_queen(self, cur_rows, n, ans):
        if len(cur_rows) == n:
            ans.append(cur_rows)
            return
        
        for i in range(n):
            if self.check_above_rows(i, cur_rows, n):
                row = ('.' * i) + 'Q' + ('.' * (n - i -1))
                self.put_queen(cur_rows + [row], n, ans)
                
                
    def check_above_rows(self, pos, cur_rows, n):
        for idx, row in enumerate(reversed(cur_rows)):
            diff = idx + 1
            if (pos - diff >= 0 and row[pos - diff] == 'Q') or \
                (pos + diff < n and row[pos + diff] == 'Q') or \
                (row[pos] == 'Q'):
                return False
        
        return True
