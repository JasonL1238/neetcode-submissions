"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root is None:
            return root 
        q = deque()
        q.append(root)
        layer = 0
        
        while q:
            layer = len(q)
            for i in range(layer):
                node = q.popleft()
                if i < layer-1:
                    node.next = q[0]
                
                if node.right is not None:
                    q.append(node.left)
                    q.append(node.right)

        return root
        


        