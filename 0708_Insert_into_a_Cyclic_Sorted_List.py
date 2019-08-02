"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head is None:
            return Node(insertVal)
    
        cur = head
        while True:
            if cur.val <= insertVal <= cur.next.val or \
                (cur.val > cur.next.val and (insertVal > cur.val or insertVal < cur.next.val)):
                cur_next = cur.next
                cur.next = Node(insertVal)
                cur.next.next = cur_next
                break
            if cur.next == head:
                cur.next = Node(insertVal)
                cur.next.next = head
                break
        
            cur = cur.next
        
        return head
