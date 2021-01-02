class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        p1 = 0
        count_k = 0
        ans = 0
        
        for p2 in range(len(A)):
            if A[p2] == 0:
                count_k += 1
                
                if count_k > K:
                    while p1 <= p2:
                        if A[p1] == 0:
                            count_k -= 1
                            break
                        p1 += 1
                        
                    p1 += 1
                        
            ans = max(ans, p2 - p1 + 1)
            
        return ans
                    
                        
