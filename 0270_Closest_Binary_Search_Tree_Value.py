# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.ans = root.val
        self.min_diff = abs(root.val - target)
        
        self.inorder(root, target)
        return self.ans
    
    
    def inorder(self, node, target):
        if node is None:
            return None
        
        diff = abs(node.val - target)
        if diff < self.min_diff:
            self.min_diff = diff
            self.ans = node.val
        
        self.inorder(node.left, target)
        self.inorder(node.right, target)
