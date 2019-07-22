# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        cur = head
        length = 0
        
        # Get length of the list
        while cur:
            length += 1
            cur = cur.next
        
        # Go middle node of the list
        cur = head
        for _ in range(length/2):
            cur = cur.next
        
        # Set None for the `next` of middle node
        cur_next = cur.next
        cur.next = None
        cur = cur_next
        
        # Put second half nodes in stack to get reversed order
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next
    
        # Interweave first half and reversed second half.
        cur = head
        while stack:
            cur_next = cur.next
            cur.next = stack.pop()
            cur.next.next = cur_next
            cur = cur_next
