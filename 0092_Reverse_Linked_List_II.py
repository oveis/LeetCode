# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        
        stack = []
        p = pre
        
        for _ in range(m-1):
            p = p.next
        
        for _ in range(n - m +1):
            stack.append(p.next)
            p.next = p.next.next
        
        for _ in range(n - m +1):
            node = stack.pop()
            node.next = p.next
            p.next = node
            p = p.next
        
        return pre.next
                
