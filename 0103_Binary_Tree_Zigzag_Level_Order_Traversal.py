# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        level = [root]
        
        while level:
            level_val = []
            next_level = []
            
            for node in level:
                if node:
                    level_val.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)

            if level_val:
                ans.append(level_val)
            level = next_level
        
        for idx, level in enumerate(ans):
            if idx % 2 == 1:
                level.reverse()
        
        return ans
