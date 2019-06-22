class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        for idx, cur in enumerate(strs):
            if idx == 0:
                # Set the first str as base result.
                res = cur
                continue
            elif not cur:
                # If current str is None or empty, there is no common prefix.
                return ''
            
            for j in range(0, len(cur)):
                if j >= len(res):
                    break
                elif cur[j] != res[j]:
                    res = res[:j]
                    break
                elif j == len(cur)-1:
                    res = res[:j+1]
                    break
        
        return res
