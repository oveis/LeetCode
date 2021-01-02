# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        global_ver_to_nodes = defaultdict(list)
        level = [(root, 0)]
        
        while level:
            ver_to_nodes = defaultdict(list)
            next_level = []
            
            while level:
                node, ver = level.pop()
                if node is None:
                    continue
                
                ver_to_nodes[ver].append(node.val)
                next_level.append((node.left, ver - 1))
                next_level.append((node.right, ver + 1))
                
            for ver, nodes in ver_to_nodes.items():
                global_ver_to_nodes[ver] += sorted(nodes)
                
            level = next_level
        
        return [global_ver_to_nodes[ver] for ver in sorted(global_ver_to_nodes.keys())]
