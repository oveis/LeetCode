# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_diff = 0
        self.get_min_max(root)
        return self.max_diff
        
    
    def get_min_max(self, node: TreeNode) -> Tuple[int, int]:
        if node is None:
            return sys.maxsize, -sys.maxsize - 1
        elif node.left is None and node.right is None:
            return node.val, node.val
        
        left_min, left_max = self.get_min_max(node.left)
        right_min, right_max = self.get_min_max(node.right)
        
        min_val = min(left_min, right_min)
        max_val = max(left_max, right_max)
        
        self.max_diff = max(abs(min_val - node.val), abs(max_val - node.val), self.max_diff)            
        
        return min(min_val, node.val), max(max_val, node.val)
