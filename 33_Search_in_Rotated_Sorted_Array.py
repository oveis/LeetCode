class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        p1, p2 = 0, len(nums)-1
        return self.search_rec(p1, p2, nums, target)

    def search_rec(self, p1, p2, nums, target):
        mid = (p1 + p2) /2
        if nums[mid] == target:
            return mid
        
        if p1 > p2:
            return -1
        
        if nums[p1] < nums[mid]:    # Left is normally ordered.
            if nums[p1] <= target and target <= nums[mid]:
                return self.search_rec(p1, mid-1, nums, target)
            else:
                return self.search_rec(mid+1, p2, nums, target)
        elif nums[p1] > nums[mid]:  # Right is normally ordered.
            if nums[mid] <= target and target <= nums[p2]:
                return self.search_rec(mid+1, p2, nums, target)
            else:
                return self.search_rec(p1, mid-1, nums, target)
        elif nums[p1] == nums[mid]: # Left is all repeats
            if nums[mid] != nums[p2]:
                return self.search_rec(mid+1, p2, nums, target)
            else:
                res = self.search_rec(p1, mid-1, nums, target)
                if res != -1:
                    return res
                else:
                    return self.search_rec(mid+1, p2, nums, target)
        
        return -1
