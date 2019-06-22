class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(1, n):
            cur_str = ''
            num = ''
            count = 0
            
            for idx, val in enumerate(res):
                if idx == 0:
                    num = val
                    count = 1
                elif num == val:
                    count += 1
                else:
                    cur_str += str(count) + num
                    num = val
                    count = 1
            
            res = cur_str + str(count) + num
        
        return res
