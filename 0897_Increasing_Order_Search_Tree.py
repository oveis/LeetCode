# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans = TreeNode(0)
        ans.right = root
        node = ans
        
        while node.right:
            if node.right.left:
                node.right = self.make_left_as_root(node.right)
            else:
                node = node.right
        
        return ans.right
    
    
    def make_left_as_root(self, root):
        rightmost_node = root.left
        while rightmost_node.right:
            rightmost_node = rightmost_node.right
        
        new_root = root.left
        rightmost_node.right = root
        root.left = None
        
        return new_root
