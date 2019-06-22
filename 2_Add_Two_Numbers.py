# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            
            cur.next = ListNode(carry % 10)
            cur = cur.next
            
            carry /= 10
        
        return head.next
