class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq = collections.Counter(s)
        heap = [(-count, letter) for letter, count in freq.items()]
        heapq.heapify(heap)
        
        last_used = {}
        rearranged = []
        
        while heap:
            too_close = []
            neg_freq, letter = heapq.heappop(heap)
            
            while letter in last_used and len(rearranged) - last_used[letter] < k:
                too_close.append((neg_freq, letter))
                if not heap:
                    return ''
                neg_freq, letter = heapq.heappop(heap)
                
            last_used[letter] = len(rearranged)
            rearranged.append(letter)
            neg_freq += 1
            if neg_freq:
                heapq.heappush(heap, (neg_freq, letter))
            
            for item in too_close:
                heapq.heappush(heap, item)
                
            
        return ''.join(rearranged)
