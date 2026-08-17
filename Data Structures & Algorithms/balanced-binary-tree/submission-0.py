# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node:Optional[TreeNode]) -> Tuple[int,bool]:
            if node == None:
                return (0,True)

            left = dfs(node.left)
            right = dfs(node.right)
            
            equal = left[1] and right[1]

            if left[0] - right[0] > 1 or left[0] - right[0] < -1:
                equal = False


            return (1+max(left[0],right[0]),equal)
        
        arr = dfs(root)
        return arr[1]
        

        
