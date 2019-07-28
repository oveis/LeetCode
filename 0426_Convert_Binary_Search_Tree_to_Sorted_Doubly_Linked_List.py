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
        
        stack = []
        self.inorder(root, stack)
        
        for idx in range(1, len(stack)):
            stack[idx-1].right = stack[idx]
            stack[idx].left = stack[idx-1]
        
        stack[0].left = stack[-1]
        stack[-1].right = stack[0]
        return stack[0]
            
        
    def inorder(self, node, stack):
        if node is None:
            return
        
        self.inorder(node.left, stack)
        stack.append(node)
        self.inorder(node.right, stack)
