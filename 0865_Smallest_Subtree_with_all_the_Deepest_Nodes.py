# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if node is None:
                return 0, None
            
            l_depth, l_node = dfs(node.left)
            r_depth, r_node = dfs(node.right)
            
            if l_depth == r_depth:
                return l_depth + 1, node
            elif l_depth > r_depth:
                return l_depth + 1, l_node
            else:
                return r_depth + 1, r_node
            
        _, node = dfs(root)
        return node
