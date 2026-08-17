# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        def depth(node:TreeNode, m:int) -> None:
            nonlocal count
            
            if node == None:
                return
            
            if node.val >= m:
                count += 1
            
            m = max(m,node.val)
            
            depth(node.left,m)
            depth(node.right,m)
            
            return None
        depth(root,-1000)
        return count
