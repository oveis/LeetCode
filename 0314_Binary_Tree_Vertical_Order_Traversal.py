# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = [(0, root)]
        
        for i, node in queue:
            if node:
                cols[i].append(node.val)
                queue += (i-1, node.left), (i+1, node.right)
                
        return [cols[i] for i in sorted(cols)]
