# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head
        
        p1 = ans
        p2 = head
        
        while p2 and p2.next:
            p1.next = p2.next
            p2.next = p2.next.next
            p1.next.next = p2
            
            p1 = p2
            p2 = p2.next
        
        return ans.next
