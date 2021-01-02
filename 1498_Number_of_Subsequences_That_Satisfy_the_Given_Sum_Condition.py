class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        p1, p2 = 0, len(nums) - 1
        count = 0
        
        while p1 <= p2:
            if nums[p1] + nums[p2] > target:
                p2 -= 1
            else:
                count += 2 ** (p2 - p1)
                count %= 10 ** 9 + 7
                p1 += 1
                
        return count
