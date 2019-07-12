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
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if not node.children:
                ans.append(node.val)
            else:
                stack.append(node)
                if node.children:
                    for child in node.children[::-1]:
                        stack.append(child)
                        
                node.children = []
        
        return ans
