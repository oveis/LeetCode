class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        upper, lower = [], []
        
        for i in range(k):
            heapq.heappush(upper, nums[i])
        
        for i in range(k/2):
            heapq.heappush(lower, -heapq.heappop(upper))
        
        odd = k % 2
        ans = []
        junk = collections.Counter()
        
        for i in range(k, len(nums)):
            ans.append(upper[0] if odd else (upper[0] - lower[0]) / 2.0)
            balance = 0
            
            if nums[i - k] >= upper[0]:
                balance -= 1
            else:
                balance += 1
            junk[nums[i - k]] += 1
            
            if nums[i] >= upper[0]:
                balance += 1
                heapq.heappush(upper, nums[i])
            else:
                balance -= 1
                heapq.heappush(lower, -nums[i])
                
            if balance > 0:
                heapq.heappush(lower, -heapq.heappop(upper))
            elif balance < 0:
                heapq.heappush(upper, -heapq.heappop(lower))
            
            while upper and junk[upper[0]] > 0:
                junk[upper[0]] -= 1
                heapq.heappop(upper)
            
            while lower and junk[-lower[0]] > 0:
                junk[-lower[0]] -= 1
                heapq.heappop(lower)
            
        ans.append(upper[0] if odd else (upper[0] - lower[0]) / 2.0)
        return ans
