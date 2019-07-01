class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = []
        for i in range(0, n+1):
            if i in [0, 1]:
                counts.append(1)
            else:
                counts.append(counts[-1] + counts[-2])
        
        return counts[-1]
