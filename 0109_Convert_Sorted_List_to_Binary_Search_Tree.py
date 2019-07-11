# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = self.get_length(head)
        
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(head.val)
        
        p = head
        for _ in range(length/2-1):
            p = p.next
        
        root = TreeNode(p.next.val)
        root.right = self.sortedListToBST(p.next.next)
        p.next = None
        root.left = self.sortedListToBST(head)
        return root
    
    
    def get_length(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
