# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return ','.join(self.get_preorder(root))
    
    
    def get_preorder(self, node):
        if not node:
            return []
    
        left = self.get_preorder(node.left)
        right = self.get_preorder(node.right)
        return [str(node.val)] + left + right
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        preorder = [int(x) for x in data.split(',')]
        return self.get_bst(preorder)
    
        
    def get_bst(self, preorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        idx = 1
        while idx < len(preorder) and preorder[idx] < root.val:
            idx += 1

        root.left = self.get_bst(preorder[1:idx])
        root.right = self.get_bst(preorder[idx:])
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
