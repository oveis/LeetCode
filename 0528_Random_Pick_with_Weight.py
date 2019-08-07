class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cumulative = []
        total = 0
        for x in w:
            total += x
            self.cumulative.append(total)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        x = random.randint(1, self.cumulative[-1])
        return bisect.bisect_left(self.cumulative, x)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
