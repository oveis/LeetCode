class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ans = 0
        p1 = 0
        for p2 in range(len(A)):
            K -= 1 - A[p2]
            
            if K < 0:
                K += 1 - A[p1]
                p1 += 1
            
            ans = max(ans, p2 - p1 + 1)
            
        return ans
