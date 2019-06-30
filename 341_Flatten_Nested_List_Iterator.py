# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flatten_list = self.get_flatten_list(nestedList)
        self.cur_pos = 0
        

    def get_flatten_list(self, nested_list):
        flatten_list = []
        for elm in nested_list:
            if elm.isInteger():
                flatten_list.append(elm.getInteger())
            else:
                flatten_list += self.get_flatten_list(elm.getList())
        return flatten_list
        
        
    def next(self):
        """
        :rtype: int
        """
        ans = self.flatten_list[self.cur_pos]
        self.cur_pos += 1
        return ans
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur_pos < len(self.flatten_list):
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
