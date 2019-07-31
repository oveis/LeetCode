# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
    
        i = 0
        while i < len(s) and s[i] != '(':
            i += 1
        
        root = TreeNode(int(s[:i]))
        
        left_start = i
        left_par = right_par = 0
        
        while i < len(s):
            if s[i] == '(':
                left_par += 1
            elif s[i] == ')':
                right_par += 1
            
            if left_par == right_par:
                break
            i += 1
        
        left_end = i
        
        root.left = self.str2tree(s[left_start+1:left_end])
        root.right = self.str2tree(s[left_end+2:-1])
        return root
