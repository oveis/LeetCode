class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []
        
        for log in logs:
            f_id, proc, time = log.split(':')
            f_id, time = int(f_id), int(time)
            
            if proc == 'start':
                if stack:
                    ans[stack[-1][0]] += time - stack[-1][1]
                    
                stack.append([f_id, time])
            else:
                ans[stack[-1][0]] += time - stack[-1][1] + 1
                stack.pop()
                
                if stack:
                    stack[-1][1] = time + 1
                    
        return ans
