"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def dfs(node):
            # print(head.val)
            cur = node
            tail = None

            while cur != None:
                if cur.child:
                    c_tail = dfs(cur.child)
                    cur_next = cur.next
                    cur.next = cur.child
                    cur.child = None
                    cur.next.prev = cur
                    
                    c_tail.next = cur_next
                    if cur_next:
                        cur_next.prev = c_tail
                        
                    cur = c_tail

                tail = cur
                cur = cur.next
        
            return tail
        
        dfs(head)
        return head
