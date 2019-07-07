from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        counter = Counter(p)
        p1 = p2 = 0
        
        while p2 < len(s):
            if s[p2] not in counter:
                while p1 < p2:
                    if s[p1] in counter:
                        counter[s[p1]] += 1
                    p1 += 1
                p2 = p1 = p2 + 1
            elif counter[s[p2]] > 0:
                counter[s[p2]] -= 1
                p2 += 1
                
                if p2 - p1 == len(p):
                    ans.append(p1)
            else:
                counter[s[p1]] += 1
                p1 += 1
                
        return ans
