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
        if root is None:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                if node.left is None and node.right is None:
                    ans.append(node.val)
                else:
                    stack.append(node)
                    stack.append(node.right)
                    stack.append(node.left)

                    node.left = None
                    node.right = None
        
        return ans
