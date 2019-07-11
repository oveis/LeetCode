# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        pre = TreeNode(0)
        pre.right = root
        node = pre
        
        while node:
            if node.left:
                rightmost_node = node.left
                while rightmost_node.right:
                    rightmost_node = rightmost_node.right
                
                rightmost_node.right = node.right
                node.right = node.left
                node.left = None
            
            node = node.right
        
        return pre.right
        
