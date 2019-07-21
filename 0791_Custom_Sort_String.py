class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        S_set = set(S)
        counter = collections.Counter()
        ans = []
        
        for t in T:
            if t in S_set:
                ans.append(' ')
                counter[t] += 1
            else:
                ans.append(t)
        
        permute = []
        for s in S:
            if s in counter:
                permute += [s] * counter[s]
        
        for idx in range(len(ans)):
            if ans[idx] == ' ':
                ans[idx] = permute.pop(0)
        
        return ''.join(ans)
