class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counter_T = collections.Counter(T)
        ans = []
        for s in S:
            if s in counter_T:
                ans += [s] * counter_T[s]
                counter_T.pop(s)
        
        for ch, counts in counter_T.items():
            ans += [ch] * counts
            
        return ''.join(ans)
