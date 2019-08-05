class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices) // 2:
            return sum([max(0, prices[i] - prices[i-1]) for i in range(1, len(prices))])
        
        buys, sells = [float('-inf')] * (k + 1), [0] * (k + 1)
        
        for price in prices:
            for i in range(1, len(buys)):
                buys[i] = max(buys[i], sells[i-1] - price)
                if buys[i] == buys[i-1]:
                    break
                sells[i] = max(sells[i], buys[i] + price)
    
        return max(sells)
