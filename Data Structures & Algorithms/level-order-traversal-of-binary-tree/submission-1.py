# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        output = []
        curr = deque()
        curr.append(root)
        layer = []
        n = []

        while curr:
            node = curr.popleft()
            layer.append(node.val)
            if node.left:
                n.append(node.left)
            if node.right:
                n.append(node.right)
            
            if not curr:
                curr.extend(n)
                n.clear()
                output.append(layer)
                layer = []
        
        return output


