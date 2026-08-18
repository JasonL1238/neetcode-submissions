class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        m = dict()
        notVisited = set()

        for u,v in edges:
            if not u in m:
                m[u] = set()
            m[u].add(v)
            if not v in m:
                m[v]= set()
            m[v].add(u)

        for i in range(n):
            notVisited.add(i)

        def dfs(node:int):
            notVisited.discard(node)
            if node in m:
                for i in m[node]:
                    if i in notVisited:
                        dfs(i)


        count = 0
        while len(notVisited)>0:
            n = notVisited.pop()
            dfs(n,)
            count += 1
        return count


            

            

