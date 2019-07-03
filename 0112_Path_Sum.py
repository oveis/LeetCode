# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.find_target_num(root, 0, sum)

    
    def find_target_num(self, node, cur_sum, sum):
        if node is None:
            return False
        elif node.left == None and node.right == None:
            return node.val + cur_sum == sum
        
        cur_sum += node.val
        return self.find_target_num(node.left, cur_sum, sum) or \
                self.find_target_num(node.right, cur_sum, sum)
