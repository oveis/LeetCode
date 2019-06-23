# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res_head = ListNode(0)
        
        while head is not None:
            tmp = head
            head = head.next
            
            tmp.next = res_head.next
            res_head.next = tmp
        
        return res_head.next
