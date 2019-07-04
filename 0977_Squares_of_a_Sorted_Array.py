class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        stack = []
        
        for a in A:
            a_2 = a ** 2
            if a < 0:
                stack.append(a_2)
            else:
                while stack and stack[-1] < a_2:
                    ans.append(stack.pop())
                ans.append(a ** 2)
                
        while stack:
            ans.append(stack.pop())
        
        return ans
