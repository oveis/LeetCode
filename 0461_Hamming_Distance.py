class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor_num = x ^ y
        
        dis = 0
        while xor_num > 0:
            dis += xor_num & 1
            xor_num >>= 1
        
        return dis
