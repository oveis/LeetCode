class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        # self.R, self.C = R, C
        # ans = []
        
        r, c = r0, c0
        # self.update_ans(r, c, ans)
        ans = [(r, c)]
        k = 1
        
        while len(ans) < R * C:
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):
                for _ in range(dk):
                    r += dr
                    c += dc
                    
                    if 0 <= r < R and 0 <= c < C:
                        ans.append((r, c))
            k += 2
            
        return ans
