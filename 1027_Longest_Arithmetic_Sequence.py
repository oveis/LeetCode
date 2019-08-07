class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sequences = [collections.Counter() for _ in range(len(A))]
        
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                sequences[i][diff] = max(sequences[j][diff] + 1, sequences[i][diff])
        
        return max(max(seq.values()) for seq in sequences[1:]) + 1
