class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_queue = []
        
        for num in nums:
            if len(k_queue) < k:
                self.insert_num(num, k_queue, k)
            elif num > k_queue[0]:
                k_queue.pop(0)
                self.insert_num(num, k_queue, k)
        
        return k_queue[0]
                
    
    def insert_num(self, num, k_queue, k):
        insert_idx = len(k_queue)
        for idx, val in enumerate(k_queue):
            if num < val:
                insert_idx = idx
                break
        k_queue.insert(insert_idx, num)
