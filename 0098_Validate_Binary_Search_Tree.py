# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = []
        self.get_inorder(root, inorder)
        
        for idx in range(1, len(inorder)):
            if inorder[idx-1] >= inorder[idx]:
                return False
        
        return True
    
    
    def get_inorder(self, node, inorder):
        if node is None:
            return
        
        self.get_inorder(node.left, inorder)
        inorder.append(node.val)
        self.get_inorder(node.right, inorder)
