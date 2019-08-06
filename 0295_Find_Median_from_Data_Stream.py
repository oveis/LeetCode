class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []
        self.upper = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.lower or self.lower[0] < -num:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)
        
        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.lower) < len(self.upper):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
                

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        else:
            return (-self.lower[0] + self.upper[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
