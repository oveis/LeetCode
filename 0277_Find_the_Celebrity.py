# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = [True] * n
        count_non = 0
        
        for i in range(n):
            for j in range(n):
                if i != j and knows(i, j):
                    candidates[i] = False
                    count_non += 1
                    break
                    
        if n - count_non > 1:
            return -1
        
        for i in range(n):
            if candidates[i]:
                continue
                
            for j in range(n):
                if candidates[j] and not knows(i, j):
                    candidates[j] = False
        
        for i in range(n):
            if candidates[i]:
                return i
        
        return -1
