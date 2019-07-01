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
        if not root:
            return ''
        
        level = [root]
        val_list = [str(root.val)]
        
        while level:
            level_len = len(level)
            
            for _ in range(level_len):
                node = level.pop(0)
                if node:
                    level.append(node.left)
                    level.append(node.right)
            
            for node in level:
                val = str(node.val) if node else 'null'
                val_list.append(val)

        return ','.join(val_list)
    
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        val_list = data.split(',')
        root = TreeNode(val_list.pop(0))
        level = [root]
        
        while level:
            node = level.pop(0)
            left_val = val_list.pop(0)
            right_val = val_list.pop(0)
            
            if left_val != 'null':
                node.left = TreeNode(left_val)
                level.append(node.left)
            
            if right_val != 'null':
                node.right = TreeNode(right_val)
                level.append(node.right)
            
        return root
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
