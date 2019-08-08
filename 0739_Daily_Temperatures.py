class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        
        for idx, temp in enumerate(T):
            while stack and stack[-1][0] < temp:
                _, prev_i = stack.pop()
                ans[prev_i] = idx - prev_i
            
            stack.append((temp, idx))
        
        return ans
