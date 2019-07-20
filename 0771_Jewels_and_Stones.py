class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set()
        for j in J:
            jewels.add(j)
        
        ans = 0
        for s in S:
            if s in jewels:
                ans += 1
        
        return ans
