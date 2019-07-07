class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack or x < self.stack[self.min_stack[-1]]:
            self.min_stack.append(len(self.stack)-1)
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return None
        
        if self.min_stack[-1] == len(self.stack)-1:
            self.min_stack.pop()
        
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.stack[self.min_stack[-1]]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
