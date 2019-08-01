# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        ans = []
        self.go_down(target, K, ans)
        self.dfs(root, target, K, ans)
        return ans
        
        
    def dfs(self, node, target, K, ans):
        if node == target:
            return K-1
        elif node is None:
            return -1
        
        left = self.dfs(node.left, target, K, ans)
        right = self.dfs(node.right, target, K, ans)
        
        if left == 0 or right == 0:
            ans.append(node.val)
        elif left != -1:
            self.go_down(node.right, left-1, ans)
            return left - 1
        elif right != -1:
            self.go_down(node.left, right-1, ans)
            return right - 1
        
        return -1
                
    
    def go_down(self, node, K, ans):
        if node is None:
            return
        elif K == 0:
            ans.append(node.val)
            return
    
        self.go_down(node.left, K-1, ans)
        self.go_down(node.right, K-1, ans)
