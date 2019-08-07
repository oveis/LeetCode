class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        count1 = collections.Counter(s1)
        count2 = collections.Counter()
        
        p = 0
        while p < len(s2):
            count2[s2[p]] += 1
            
            if p >= len(s1):
                remove = s2[p - len(s1)]
                count2[remove] -= 1
                if count2[remove] == 0:
                    count2.pop(remove)
            
            if count1 == count2:
                return True
            
            p += 1
            
        return False
