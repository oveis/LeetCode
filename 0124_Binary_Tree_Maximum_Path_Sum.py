# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = root.val
        self.get_max_path_sum(root)
        return self.ans
    
    
    def get_max_path_sum(self, node):
        if node is None:
            return float('-inf')
        
        left = self.get_max_path_sum(node.left)
        right = self.get_max_path_sum(node.right)
        
        self.ans = max(self.ans, \
                       left, node.val, right, \
                       left + node.val, right + node.val, \
                       left + node.val + right
                      )
        return max(node.val, left + node.val, right + node.val)
