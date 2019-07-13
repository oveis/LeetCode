"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ans = Node(0, None, None)
        clone = ans
        origin = head
        
        origin_list = []
        clone_list = []
        
        while origin != None:
            clone.next = Node(origin.val, None, None)
            clone = clone.next
            clone_list.append(clone)
            
            origin_list.append(origin)
            origin = origin.next
        
        for idx, origin in enumerate(origin_list):
            if not origin.random:
                continue
            
            clone = clone_list[idx]
            random_idx = self.find_node_from_list(origin.random, origin_list)
            
            if random_idx == -1:
                clone.random = Node(origin.random.val, None, None)
                clone_list.append(clone.random)
                origin_list.append(origin.random)
            else:
                clone.random = clone_list[random_idx]
                
        return ans.next
    
    
    def find_node_from_list(self, node, node_list):
        for idx, val in enumerate(node_list):
            if val == node:
                return idx
        return -1
