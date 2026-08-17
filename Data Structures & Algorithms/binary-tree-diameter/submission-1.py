# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    

        def miniTree(root) -> List:
            
            if root == None:
                return [0,0]

            leftH = miniTree(root.left)
            rightH = miniTree(root.right)

            maxD = max(leftH[0],rightH[0],leftH[1]+rightH[1])

            print(maxD)

            return [maxD,1+max(leftH[1],rightH[1])]


        arr = miniTree(root) 
        return arr[0]