"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        ans = []
        self.get_postorder(root, ans)
        return ans
    
    
    def get_postorder(self, node, ans):
        
        if node.children:
            for child in node.children:
                self.get_postorder(child, ans)
        
        ans.append(node.val)
