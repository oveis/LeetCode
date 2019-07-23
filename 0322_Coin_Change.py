class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        counts = [float('inf')] * (amount + 1)
        counts[0] = 0
        
        for i in range(1, amount+1):
            if i in coins:
                counts[i] = 1
            else:
                for coin in coins:
                    if i - coin >= 0:
                        counts[i] = min(counts[i], counts[i-coin]+1)
        
        return -1 if counts[-1] == float('inf') else counts[-1]
