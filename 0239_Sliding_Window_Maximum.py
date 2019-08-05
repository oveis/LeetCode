class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        heap = [-nums[i] for i in range(k)]
        heapq.heapify(heap)
        
        ans = []
        dummy = collections.Counter()
        
        for i in range(k, len(nums)):
            ans.append(-heap[0])
            
            dummy[nums[i-k]] += 1
            heapq.heappush(heap, -nums[i])
            
            while heap and dummy[-heap[0]] > 0:
                remove = heapq.heappop(heap)
                dummy[-remove] -= 1
                
        ans.append(-heap[0])
        return ans
