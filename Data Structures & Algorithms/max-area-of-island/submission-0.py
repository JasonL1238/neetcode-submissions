class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = 0
        s = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not (row,col) in s and grid[row][col] == 1:
                    q = deque()
                    q.append((row,col))
                    count = 0
                    while q:
                        r,c = q.popleft()
                        if not (r,c) in s:
                            if c < len(grid[row])-1 and grid[r][c+1] == 1:
                                q.append((r,c+1))
                            if c > 0 and grid[r][c-1] == 1:
                                q.append((r,c-1))
                            if r < len(grid)-1 and grid[r+1][c] == 1:
                                q.append((r+1,c))
                            if r >0 and grid[r-1][c] == 1:
                                q.append((r-1,c))
                            s.add((r,c))
                            count += 1

                    m = max(m,count)
            
        return m

                        
                    
        