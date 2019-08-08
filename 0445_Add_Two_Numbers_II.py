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
        s1 = self.conv_stack(l1)
        s2 = self.conv_stack(l2)
        
        head = ListNode(0)
        carry = 0
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            
            tmp = head.next
            head.next = ListNode(carry % 10)
            head.next.next = tmp
            
            carry /= 10
            
        return head.next
            
    
    def conv_stack(self, l):
        stack = []
        cur = l
        while cur:
            stack.append(cur.val)
            cur = cur.next
        return stack
