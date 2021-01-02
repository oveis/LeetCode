class SparseVector:
    def __init__(self, nums: List[int]):
        self.pos_to_val = dict()
        for idx, num in enumerate(nums):
            if num != 0:
                self.pos_to_val[idx] = num
                

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for idx, val in vec.pos_to_val.items():
            if idx in self.pos_to_val:
                ans += val * self.pos_to_val[idx]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
