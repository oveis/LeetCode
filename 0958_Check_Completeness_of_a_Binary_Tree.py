# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        
        queue = [root]
        
        is_hit_end = False
        while queue:
            next_queue = []
            
            for node in queue:
                if node:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            
            for node in next_queue:
                if node is None:
                    is_hit_end = True
                    
                if is_hit_end and node:
                    return False
        
            queue = next_queue
            
        return True
