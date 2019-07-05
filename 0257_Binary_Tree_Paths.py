# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        output = []
        
        self.get_paths(root, path, output)
        return output
    
    
    def get_paths(self, node, path, output):
        if node is None:
            return
        
        path.append(str(node.val))
        
        if node.left == None and node.right == None:
            output.append('->'.join(path))
        else:
            self.get_paths(node.left, path, output)
            self.get_paths(node.right, path, output)
        
        path.pop()
