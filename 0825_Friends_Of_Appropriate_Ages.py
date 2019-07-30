class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        ans = 0
        for A, countA in enumerate(count):
            for B, countB in enumerate(count):
                if (B <= 0.5 * A + 7) or (B > A) or (A < 100 < B):
                    continue
                
                ans += countA * countB
                
                if A == B:
                    ans -= countB
            
        return ans
