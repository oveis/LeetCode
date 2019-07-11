# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.get_postorder(root, ans)
        return ans
    
    
    def get_postorder(self, node, ans):
        if node is None:
            return
        
        self.get_postorder(node.left, ans)
        self.get_postorder(node.right, ans)
        ans.append(node.val)
