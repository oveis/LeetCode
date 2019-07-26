class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        odd = ['0', '1', '8']
        even = ['00', '11', '88', '69', '96']
        
        if n % 2 == 0:
            queue = copy.deepcopy(even)
        else:
            queue = copy.deepcopy(odd)
            
        while len(queue[0]) < n:
            new_queue = []
            
            while queue:
                num = queue.pop()
                for val in even:
                    new_num = val[0] + num + val[1]
                    new_queue.append(val[0] + num + val[1])
            
            queue = new_queue
        
        if n == 1:
            return queue
        else:
            return [x for x in queue if x[0] != '0']
