# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None:
            return True
        elif s == None:
            return False
        
        if self.check_subtree(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    
    def check_subtree(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None or node1.val != node2.val:
            return False
        
        return self.check_subtree(node1.left, node2.left) and \
                self.check_subtree(node1.right, node2.right)
