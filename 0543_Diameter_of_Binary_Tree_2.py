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
        self.ans = 0
        self.depth(root)
        return self.ans
    
    
    def depth(self, node):
        if node is None:
            return 0

        left = self.depth(node.left)
        right = self.depth(node.right)

        self.ans = max(self.ans, left + right)
        return max(left, right) + 1
