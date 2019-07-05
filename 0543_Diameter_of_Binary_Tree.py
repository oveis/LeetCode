# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, diameter = self.get_height_and_diameter(root)
        return diameter
        
        
    def get_height_and_diameter(self, node):
        if node is None:
            return 0, 0
        
        left_height, left_diameter = self.get_height_and_diameter(node.left)
        right_height, right_diameter = self.get_height_and_diameter(node.right)
        
        max_diameter = max(left_diameter, right_diameter, left_height + right_height)
        
        return max(left_height, right_height) + 1, max_diameter
