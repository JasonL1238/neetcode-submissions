class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        s = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col]
                if cell == 0:
                    s.clear()
                    grid[row][col] = 0
                    q = deque()
                    count = 1
                    q.append((row,col))
                    while q:
                        for k in range(len(q)):
                            r,c = q.popleft()
                            if r < len(grid)-1 and not (r+1,c) in s and grid[r+1][c] > 0:
                                grid[r+1][c] = min(count,grid[r+1][c])
                                q.append((r+1,c))
                            if c < len(grid[0])-1 and not (r,c+1) in s and grid[r][c+1] > 0:
                                grid[r][c+1] = min(count,grid[r][c+1])
                                q.append((r,c+1))
                            if r > 0 and not (r-1,c) in s and grid[r-1][c] > 0:                                
                                grid[r-1][c] = min(count,grid[r-1][c])
                                q.append((r-1,c))
                            if c > 0 and not (r,c-1) in s and grid[r][c-1] > 0:
                                grid[r][c-1] = min(count,grid[r][c-1])
                                q.append((r,c-1))
                            s.add((r,c))
                        count +=1







