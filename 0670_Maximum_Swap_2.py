class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = []
        while num > 0:
            num_list.insert(0, num % 10)
            num //= 10
        
        max_nums = []
        for idx in range(len(num_list) - 1, -1, -1):
            if not max_nums or max_nums[0][0] < num_list[idx]:
                max_nums.insert(0, (num_list[idx], idx))
            else:
                max_nums.insert(0, max_nums[0])
        
        for idx, n in enumerate(num_list):
            if n < max_nums[idx][0]:
                num_list[idx] = max_nums[idx][0]
                num_list[max_nums[idx][1]] = n
                break
                
        ans = 0
        for n in num_list:
            ans = ans * 10 + n
        
        return ans
