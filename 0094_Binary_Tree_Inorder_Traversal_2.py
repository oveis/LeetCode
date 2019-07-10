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
        if root is None:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node is None:
                continue
                
            if node.left == None and node.right == None:
                ans.append(node.val)
            else:
                node_left = node.left
                node_right = node.right
                node.left = None
                node.right = None

                stack.append(node_right)
                stack.append(node)
                stack.append(node_left)
                    
        return ans
