from decimal import Decimal
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        
        ans = 2
        
        for i, point1 in enumerate(points):
            gradients = collections.Counter()
            max_points = 1
            
            for point2 in points[i+1:]:
                if point1[0] == point2[0]:
                    if point1[1] == point2[1]:
                        max_points += 1
                    else:
                        gradients['inf'] += 1
                else:
                    dex = point2[0] - point1[0]
                    dey = point2[1] - point1[1]
                    d = self.gcd(dex, dey)
                    gradients[(dex/d, dey/d)] += 1
            
            if gradients:
                max_points += max(gradients.values())
            
            ans = max(ans, max_points)
        
        return ans
                
        
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
