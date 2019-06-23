class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        high_prices = []
        for price in reversed(prices):
            if len(high_prices) == 0 or price > high_prices[-1]:
                high_prices.append(price)
            else:
                high_prices.append(high_prices[-1])
        
        high_prices.reverse()
        
        low_prices = []
        for price in prices:
            if len(low_prices) == 0 or price < low_prices[-1]:
                low_prices.append(price)
            else:
                low_prices.append(low_prices[-1])
        
        max_profit = 0
        for i in range(0, len(prices)):
            max_profit = max(max_profit, high_prices[i] - low_prices[i])
        
        return max_profit
