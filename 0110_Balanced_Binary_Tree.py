# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = True
        self.get_depth(root)
        
        return self.ans
        
    
    def get_depth(self, node):
        if node is None:
            return 0
        
        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)
        
        if abs(left_depth - right_depth) > 1:
            self.ans = False
            
        return max(left_depth, right_depth) + 1
