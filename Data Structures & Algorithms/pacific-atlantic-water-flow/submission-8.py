class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])
        output = []

        p = set()
        a = set()
        sources = deque()

        for i in range(m):
            p.add((i,0))
            a.add((i,n-1))
        for i in range(n):
            p.add((0,i))
            a.add((m-1,i))

        print(p)
        print(a)

        for k in p:
            sources.append(k)
        p.clear()
        
        
        while sources:
            r,c = sources.popleft()
            if not (r,c) in p:
                node = heights[r][c]
                if r > 0 and heights[r-1][c] >= node: 
                    sources.append((r-1,c)) 
                if c > 0 and heights[r][c-1] >= node: 
                    sources.append((r,c-1)) 
                if r < m-1 and heights[r+1][c] >= node: 
                    sources.append((r+1,c))              
                if c < n-1 and heights[r][c+1] >= node: 
                    sources.append((r,c+1))
                p.add((r,c))

        print(sources)
        
        for i in a:
            sources.append(i)
        a.clear()
        print(sources)

        while sources:
            r,c = sources.popleft()
            if not (r,c) in a:
                node = heights[r][c]
                if r > 0 and heights[r-1][c] >= node: 
                    sources.append((r-1,c)) 
                if c > 0 and heights[r][c-1] >= node: 
                    sources.append((r,c-1)) 
                if r < m-1 and heights[r+1][c] >= node: 
                    sources.append((r+1,c))              
                if c < n-1 and heights[r][c+1] >= node: 
                    sources.append((r,c+1))
                a.add((r,c))

        for i in range(len(heights)):
            for k in range(len(heights[i])):
                if (i,k) in a and (i,k) in p:
                    output.append([i,k])
        
        return output
