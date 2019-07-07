class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1 = n2 = n3 = -sys.maxint - 1
        num_set = set()
        
        for num in nums:
            if num in num_set:
                continue
            else:
                num_set.add(num)

            if num > n1:
                n3 = n2
                n2 = n1
                n1 = num
            elif num > n2:
                n3 = n2
                n2 = num
            elif num > n3:
                n3 = num
        
        return n3 if len(num_set) >=3 else n1
