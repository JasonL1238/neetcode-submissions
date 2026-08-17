# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node: Optional[TreeNode]) -> Tuple[int,int]:
            
            if node == None:
                return (-10000,0)
            
            left = dfs(node.left)
            right = dfs(node.right)

            path = max(left[1],right[1],0) + node.val

            m = max(left[0],right[0],node.val+left[1]+right[1],node.val,node.val+left[1],node.val+right[1])

            return (m,path)


        
        return dfs(root)[0]
            
