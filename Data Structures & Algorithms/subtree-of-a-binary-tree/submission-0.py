# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p == None or q == None:
                return p == q
            elif not p.val == q.val:
                return False
            else:
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        if root == None:
            return subRoot == None

        if root.val == subRoot.val:
            if isSameTree(root,subRoot):
                return True
        
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)

        return left or right




