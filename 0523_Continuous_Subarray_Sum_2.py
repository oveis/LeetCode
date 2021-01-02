class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_set = set()
        for i in range(len(nums)-1, -1, -1):
            sum_set = {s + nums[i] for s in sum_set}
            
            for s in sum_set:
                if k == 0 and s == 0:
                    return True
                elif k != 0 and s % k == 0:
                    return True
                
            sum_set.add(nums[i])
                
        return False
