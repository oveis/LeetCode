class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_list = []
        for num in nums:
            for idx, n in enumerate(k_list):
                if num >= n:
                    k_list.insert(idx, num)
                    break
            else:
                k_list.append(num)
                    
            if len(k_list) > k:
                k_list.pop()
        
        return k_list[-1]
