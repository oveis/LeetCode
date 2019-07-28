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
        if root is None:
            return None
        
        head = tail = root
        
        while head.left:
            head = head.left
            
        while tail.right:
            tail = tail.right
        
        self.conv_doubly_list(root)
        
        head.left = tail
        tail.right = head
        
        return head
    
    
    def conv_doubly_list(self, node):
        if node is None:
            return
        
        pre = node.left
        while pre and pre.right:
            pre = pre.right
        
        suc = node.right
        while suc and suc.left:
            suc = suc.left
        
        self.conv_doubly_list(node.left)
        self.conv_doubly_list(node.right)
        
        node.left = pre
        if pre:
            pre.right = node
        
        node.right = suc
        if suc:
            suc.left = node
