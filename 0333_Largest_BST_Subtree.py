# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.ans_node_nums = 0
        
        self.dfs(root)
        return self.ans_node_nums
        
    
    def dfs(self, node: TreeNode) -> tuple[bool, int, int, int]:
        if node is None:
            return True, 0, 0, 0
        
        is_left_bst, left_nums, left_min, left_max = self.dfs(node.left)
        is_right_bst, right_nums, right_min, right_max = self.dfs(node.right)
        
        if is_left_bst and is_right_bst:
            if self.is_bst(node, left_max, right_min):
                node_nums = left_nums + right_nums + 1
                self.ans_node_nums = max(self.ans_node_nums, node_nums)
                    
                left_min = left_min if node.left else node.val
                right_max = right_max if node.right else node.val
                return True, node_nums, left_min, right_max
            
        return False, 0, 0, 0
    
    
    def is_bst(self, node: TreeNode, left_max: int, right_min: int) -> bool:
        return (node.left is None and node.right is None) or \
                (node.left is None and node.val < right_min) or \
                (node.right is None and left_max < node.val) or \
                (left_max < node.val < right_min)
