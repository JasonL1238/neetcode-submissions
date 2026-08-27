class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()

        m = dict()
        cycle = set()
        start = -1

        for u,v in edges:
            if not u in m:
                m[u] = []
            if not v in m:
                m[v] = []
            m[u].append(v)
            m[v].append(u)
        
        def dfs(node:int,prev:int):
            nonlocal start
            visited.add(node)
            for n in m[node]:
                if not n == prev:
                    if n in visited:
                        cycle.add((node,n))
                        start = n
                        return True
                    if dfs(n,node):
                        if n == start:
                            return False
                        cycle.add((node,n))
                        return True
            
            return False
                    
        dfs(1,-1)
        output = []
        print(cycle)
        print(start)
        for u,v in edges:
            if (u,v) in cycle or (v,u) in cycle:
                output = [u,v]
        return output




