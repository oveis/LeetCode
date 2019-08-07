# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        heap = []
        queue = [(0, 0, root)]
        while queue:
            next_queue = []
            
            while queue:
                (col, neg_row, node) = queue.pop()
                heapq.heappush(heap, (col, neg_row, node.val))
                
                if node.left:
                    next_queue.append((col-1, neg_row+1, node.left))
                if node.right:
                    next_queue.append((col+1, neg_row+1, node.right))
            
            queue = next_queue
        
        ans = []
        cur_col = heap[0][0]
        val_list = []
        
        while heap:
            (col, _, val) = heapq.heappop(heap)
            if col == cur_col:
                val_list.append(val)
            else:
                ans.append(val_list)
                cur_col = col
                val_list = [val]
        
        if val_list:
            ans.append(val_list)
            
        return ans
