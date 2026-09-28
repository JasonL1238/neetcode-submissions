class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = [[] for _ in range(n)]
        prices = dict()
        best = dict()

        for i in flights:
            adj[i[0]].append(i[1])
            index = (i[0],i[1])
            prices[index] = i[2]
        
        cost = float("inf")
        def dfs(currCost:int, node: int, l: int, prev: int):
            nonlocal cost
            if not node in best:
                best[node] = (float("inf"),k)
            

            if node == dst:
                cost = min(cost,currCost)
            elif l <= k and (currCost < best[node][0] or l < best[node][1]):
                best[node] = (currCost,l)
                for neighbor in adj[node]:
                    if not neighbor == prev:
                        newCost = currCost + prices[(node,neighbor)]
                        dfs(newCost,neighbor,l+1,node)
        dfs(0,src,0,-1)

        if cost == float("inf"):
            cost = -1
        return cost

        