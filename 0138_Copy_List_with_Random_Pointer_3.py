"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_list = []
        cur_node = head
        node_to_id = dict()
        
        while cur_node:
            node_to_id[cur_node] = len(node_list)
            node_list.append(cur_node)
            cur_node = cur_node.next
        
        cloned_node_list = []
        
        for node in node_list:
            cloned_node = Node(x=node.val)
            cloned_node_list.append(cloned_node)
            
        for idx, node in enumerate(node_list):
            cloned_node = cloned_node_list[idx]
            
            if node.random is None:
                cloned_node.random = None
            else:
                random_node_id = node_to_id[node.random]
                cloned_node.random = cloned_node_list[random_node_id]
            
            if idx + 1 < len(node_list):
                cloned_node.next = cloned_node_list[idx+1]
                
        return cloned_node_list[0] if cloned_node_list else None
