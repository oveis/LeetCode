# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a_length = self.get_length(headA)
        b_length = self.get_length(headB)
        
        while a_length > b_length:
            headA = headA.next
            a_length -= 1
        
        while a_length < b_length:
            headB = headB.next
            b_length -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        
    
    def get_length(self, node):
        length = 0
        cur = node
        
        while cur:
            length += 1
            cur = cur.next
        
        return length
