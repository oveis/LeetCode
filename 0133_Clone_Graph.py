"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not Node:
            return None
        
        origin_clone_map = dict()
        return self.get_clone_node(node, origin_clone_map)
    
        
    def get_clone_node(self, node, origin_clone_map):
        if node in origin_clone_map:
            return origin_clone_map[node]
        
        clone = Node(node.val, [])
        origin_clone_map[node] = clone
        
        for neighbor in node.neighbors:
            clone.neighbors.append(self.get_clone_node(neighbor, origin_clone_map))
        
        return clone
