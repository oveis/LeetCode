"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        first, last = self.inorder(root)
        if first and last:
            first.left = last
            last.right = first
            
        return first
        
    
    def inorder(self, node):
        if node is None:
            return None, None
        
        l_first, l_last = self.inorder(node.left)
        r_first, r_last = self.inorder(node.right)
        
        if l_last:
            l_last.right = node
            node.left = l_last
        
        if r_first:
            r_first.left = node
            node.right = r_first
            
        return (l_first or node), (r_last or node)
