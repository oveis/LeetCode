# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        p1, p2 = 0, cols - 1
        
        ans = -1
        for row in range(rows):
            p1 = 0
            p2 = cols - 1 if ans == -1 else ans - 1
                
            while p1 < p2:
                mid = (p1 + p2) // 2
                if binaryMatrix.get(row, mid) == 1:
                    p2 = mid
                else:
                    p1 = mid + 1

            if p1 == p2 and binaryMatrix.get(row, p1) == 1:
                if ans == -1 or p1 < ans:
                    ans = p1
            
        return ans
