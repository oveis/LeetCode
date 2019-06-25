class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = dict()
        
        for str in strs:
            sorted_str = ''.join(sorted(str))
            
            if sorted_str not in groups:
                groups[sorted_str] = []
            
            groups[sorted_str].append(str)
        
        return [group for _, group in groups.items()]
