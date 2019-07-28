class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        self.target = target
        
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                val = num[:i]
                self.dfs(num[i:], val, int(val), int(val), ans)
        return ans
    
    
    def dfs(self, num, cur_expr, cur_num, last, ans):
        if not num:
            if cur_num == self.target:
                ans.append(cur_expr)
            return
        
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], cur_expr + '+' + val, cur_num + int(val), int(val), ans)
                self.dfs(num[i:], cur_expr + '-' + val, cur_num - int(val), -int(val), ans)
                self.dfs(num[i:], cur_expr + '*' + val, cur_num - last + last * int(val), last * int(val), ans)
