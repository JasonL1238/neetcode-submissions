import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]

        heap = []

        for u,v,w in times:
            adj[u].append((w,v,u))
        
        for w,v,u in adj[k]:
            heapq.heappush(heap, (w, v,u))
        print(heap)
        visited = set()
        print(adj)
        cost = 0
        visited.add(k)
        while heap and len(visited) < n:
            edge = heapq.heappop(heap)
            curr = edge[1]
            par = edge[2]
            weight = edge[0]
            cost = max(cost,weight)
            visited.add(curr)
            
            for w,v,u in adj[curr]:
                if not v in visited:
                    heapq.heappush(heap, (w+weight, v,curr))
            
            while heap and heap[0][1] in visited:
                heapq.heappop(heap)

        
        if len(visited) == n:
            return cost
        
        return -1






        