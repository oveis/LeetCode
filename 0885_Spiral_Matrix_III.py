class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        self.R, self.C = R, C
        ans = []
        
        t = 1
        r, c = r0, c0
        self.update_ans(r, c, ans)
        
        while len(ans) < R * C:
            # Go right
            for _ in range(t):
                c += 1
                self.update_ans(r, c, ans)
            
            # Go down
            for _ in range(t):
                r += 1
                self.update_ans(r, c, ans)
            
            t += 1
            # Go left
            for _ in range(t):
                c -= 1
                self.update_ans(r, c, ans)
            
            # Go up
            for _ in range(t):
                r -= 1
                self.update_ans(r, c, ans)
            
            t += 1
        
        return ans
    
    
    def update_ans(self, r, c, ans):
        if r >= 0 and r < self.R and c >= 0 and c < self.C:
            ans.append([r, c])
