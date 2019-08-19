class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_count = collections.Counter()
        guess_count = collections.Counter()
        
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[secret[i]] += 1
                guess_count[guess[i]] += 1
               
        cows = 0
        for num, counts in secret_count.items():
            if num in guess_count:
                cows += min(counts, guess_count[num])
        
        return '{}A{}B'.format(bulls, cows)
