# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        queue = [root]
        while queue:
            next_queue = []
            
            for node in queue:
                if node is None:
                    continue
                    
                tmp = node.left
                node.left = node.right
                node.right = tmp
                
                next_queue.append(node.left)
                next_queue.append(node.right)
            
            queue = next_queue
        
        return root
