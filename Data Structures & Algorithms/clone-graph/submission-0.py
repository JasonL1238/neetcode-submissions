"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        head = Node(node.val)

        m = {
            node:head
        }

        q = deque()
        q.append(node)
        s = set()

        while q:
            node = q.popleft()
            if node not in s:
                n = Node(node.val)
                if node in m:
                    n = m[node]
                
                if node.neighbors:
                    for i in node.neighbors:
                        if not i in m:
                            c = Node(i.val)
                            m[i] = c                  
                        n.neighbors.append(m[i])
                        q.append(i)
                s.add(node)
            
        return head

            
