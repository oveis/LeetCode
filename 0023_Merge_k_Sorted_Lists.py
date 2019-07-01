# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        head = lists[0]
        
        for i in range(1, len(lists)):
            head = self.merge_lists(head, lists[i])
        
        return head

    
    def merge_lists(self, node1, node2):
        head = ListNode(0)
        cur = head
        
        while node1 and node2:
            if node1.val < node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next
        
        if node1:
            cur.next = node1
        if node2:
            cur.next = node2
        
        return head.next
