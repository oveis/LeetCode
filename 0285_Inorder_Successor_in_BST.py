# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root == p:
            # Get leftmost node in right child
            node = root.right
            while node and node.left:
                node = node.left
            return node
        
        if p.val > root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            return self.inorderSuccessor(root.left, p) or root
