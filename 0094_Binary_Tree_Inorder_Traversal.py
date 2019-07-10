# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.inorder(root, ans)
        return ans
    
    
    def inorder(self, node, ans):
        if node is None:
            return
        
        self.inorder(node.left, ans)
        ans.append(node.val)
        self.inorder(node.right, ans)
