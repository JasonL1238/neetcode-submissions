class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n == 1:
            return len(edges) == 0
            
        m = dict()
        dup = set()

        for u, v in edges:
            if u not in m:
                m[u] = set()
            m[u].add(v)
            if v not in m:
                m[v] = set()
            m[v].add(u)

        
        def dfs(node: int, prev: int):
            if node in dup or not node in m:
                return False
            dup.add(node)
            for i in m[node]:
                if not i == prev:
                    if not dfs(i,node):
                        return False
            return True

        output = dfs(0,-1)  
        return output and len(dup) == n
                


        