# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    cur = None
    
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans = TreeNode(0)
        self.cur = ans
        self.inorder(root)
        return ans.right
    
    
    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)
        
        node.left = None
        self.cur.right = node
        self.cur = self.cur.right
        
        self.inorder(node.right)
