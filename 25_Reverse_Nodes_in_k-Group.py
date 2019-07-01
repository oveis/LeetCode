# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        
        p1 = pre
        p2 = head
        
        while p2 != None:
            stack = []
            
            count = 0
            while count < k and p2 != None:
                stack.append(p2)
                p2 = p2.next
                count += 1
                
            if len(stack) == k:
                start_node, end_node = self.get_list_from_stack(stack)
                p1.next = start_node
                end_node.next = p2
                p1 = end_node
        
        return pre.next
    
    
    def get_list_from_stack(self, stack):
        head = ListNode(0)
        tail = head
        while stack:
            tail.next = stack.pop()
            tail = tail.next
        return head.next, tail
