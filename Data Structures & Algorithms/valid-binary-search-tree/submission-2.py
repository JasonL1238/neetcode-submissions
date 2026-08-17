# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        output = True
        
        def search(node: Optional[TreeNode]) -> Tuple[int,int]:

            nonlocal output

            if node == None:
                return (1001,-1001)
            
            left = search(node.left)
            right = search(node.right)

            minL,maxL = left
            minR,maxR = right

            if maxL > minR or maxL >= node.val or minR <= node.val:
                output = False

            print(str(left) + " left")
            print(str(right) +  " right")
            
            totalMin = min(minL,minR,node.val)
            totalMax = max(maxL,maxR,node.val)
            return (totalMin,totalMax)
        
        a = search(root)

        return output

                
