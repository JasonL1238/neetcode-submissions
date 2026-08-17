# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        o = []
        s = []

        def build(p: Optional[TreeNode],arr) -> None:

            if p == None:
                arr.append("#")
            else:
                build(p.left,arr)
                build(p.right,arr)
                arr.append(str(p.val))

        build(root,o)
        build(subRoot,s)

        str1 = "".join(o)
        str2 = "".join(s)

        return str2 in str1




