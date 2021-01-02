class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
            
        k_list = []
        for num, count in counter.items():
            for idx, (k_num, k_count) in enumerate(k_list):
                if count > k_count:
                    k_list.insert(idx, (num, count))
                    break
            else:
                k_list.append((num, count))
                
            k_list = k_list[:k]
            
        return [num for (num, count) in k_list]
