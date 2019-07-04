# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        sequence1, sequence2 = [], []
        self.get_leaf_sequence(root1, sequence1)
        self.get_leaf_sequence(root2, sequence2)
        
        return sequence1 == sequence2
    
        
    def get_leaf_sequence(self, node, sequence):
        if node is None:
            return
        elif node.left == None and node.right == None:
            sequence.append(node.val)
        
        self.get_leaf_sequence(node.left, sequence)
        self.get_leaf_sequence(node.right, sequence)
