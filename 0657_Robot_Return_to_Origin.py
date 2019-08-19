class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up = right = 0
        for move in moves:
            if move == 'U':
                up += 1
            elif move == 'D':
                up -= 1
            elif move == 'R':
                right += 1
            elif move == 'L':
                right -= 1
                
        return up == right == 0
