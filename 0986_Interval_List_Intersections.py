class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        while A and B:
            a, b = A[0], B[0]
            inter = [max(a[0], b[0]), min(a[1], b[1])]
            if inter[0] <= inter[1]:
                ans.append(inter)
            
            if a[1] > b[1]:
                B.pop(0)
            else:
                A.pop(0)
                
        return ans
