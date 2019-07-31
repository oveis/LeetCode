class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]
        rows, cols = len(board), len(board[0])
        
        target_to_sources = collections.defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                for dr, dc in [(1, 2), (1, -2), (-1, 2), (-1, -2), \
                              (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                    
                    if 0 <= i + dr < rows and 0 <= j + dc < cols and \
                        board[i][j] != None and board[i+dr][j+dc] != None:
                        
                        target, source = board[i+dr][j+dc], board[i][j]
                        target_to_sources[target].append(source)

        counts = [1] * 10
        for _ in range(1, N):
            next_counts = [0] * 10
            
            for digit, count in enumerate(counts):
                for source in target_to_sources[digit]:
                    next_counts[digit] += counts[source]
                    
            counts = next_counts
        
        return sum(counts) % (10 **9 + 7)
