class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_counts = collections.defaultdict(int)
        for num in nums:
            num_counts[num] += 1
        
        counts = [(num, count) for num, count in num_counts.items()]
        counts.sort(key=lambda x: x[1], reverse=True)
        return [num for (num, count) in counts[:k]]
