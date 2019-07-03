class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        
        for idx in range(1, len(prices)):
            if prices[idx-1] < prices[idx]:
                profit += prices[idx] - prices[idx-1]
        
        return profit
