class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        heap = [(-val, key) for key, val in count.items()]
        heapq.heapify(heap)
        
        ans = []
        while heap and k > 0:
            (neg_freq, word) = heapq.heappop(heap)
            ans.append(word)
            k -= 1
                
        return ans
