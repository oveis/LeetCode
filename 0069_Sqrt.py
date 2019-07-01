class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.search_bst(1, x, x)

    
    def search_bst(self, n1, n2, target):
        if n1 >= n2:
            return n1 if n1 ** 2 <= target else n1-1
        
        mid = (n1 + n2) / 2
        mid_pow2 = mid ** 2
        
        if mid_pow2 == target:
            return mid
        elif mid_pow2 < target:
            return self.search_bst(mid+1, n2, target)
        else:
            return self.search_bst(n1, mid-1, target)
