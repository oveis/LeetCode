class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p1 = p2 = 0
        
        p_counter = defaultdict(int)
        for c in p:
            p_counter[c] += 1
        
        ans = []
        s_counter = defaultdict(int)
        
        while p2 < len(s):
            s_counter[s[p2]] += 1
            
            if p2 - p1 + 1 < len(p):
                p2 += 1
                continue
                
            if s_counter == p_counter:
                ans.append(p1)
            
            s_counter[s[p1]] -= 1
            if s_counter[s[p1]] == 0:
                del s_counter[s[p1]]
                
            p1 += 1
            p2 += 1
            
        return ans
