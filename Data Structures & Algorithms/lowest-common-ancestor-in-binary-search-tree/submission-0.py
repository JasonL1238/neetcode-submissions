# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        path1 = []
        path2 = []

        def findPath(node: Treenode, n: TreeNode,arr: List) -> TreeNode:

            if node == None:
                return node

            if node.val == n.val:
                print(node.val)
                arr.append(node)
                return n
            

            
            left = findPath(node.left,n,arr)
            right = findPath(node.right,n,arr)

            if left == n or right == n:
                arr.append(node)
                return n
            else:
                return node
        
        a = findPath(root,p,path1)
        b = findPath(root,q,path2)



        A = path1
        B = set(path2)


        if len(path1) < len(path2):
            A = path2
            B = set(path1)



        
        for i in A:
            if i in B:
                return i
        
        return a


            
                

            




