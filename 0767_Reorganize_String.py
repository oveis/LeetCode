class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(heap)
        
        ans = ''
        while heap and len(heap) >= 2:
            new_heap = []
            for _ in range(2):
                (neg_count, char) = heapq.heappop(heap)
                ans += char
                neg_count += 1
                if neg_count != 0:
                    new_heap.append((neg_count, char))
            
            for item in new_heap:
                heapq.heappush(heap, item)

        if heap:
            (neg_count, char) = heapq.heappop(heap)
            if neg_count < -1:
                return ''
            else:
                ans += char
        
        return ans
