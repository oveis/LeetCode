class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        mask = [False] * len(s)
        
        for i in range(len(s)):
            prefix = s[i:]
            for word in dict:
                if prefix.startswith(word):
                    mask[i:i+len(word)] = [True] * len(word)
                
        res = []
        if mask[0]:
            res.append('<b>')
                
        for i in range(len(s) - 1):
            res.append(s[i])
            
            if not mask[i] and mask[i+1]:
                res.append('<b>')
            elif mask[i] and not mask[i+1]:
                res.append('</b>')
                
        res.append(s[-1])
        if mask[-1]:
            res.append('</b>')
            
        return ''.join(res)
