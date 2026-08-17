class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        s = set()

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                
                point = grid[row][col]

                if not (row,col) in s and point == "1":
                    q = deque()
                    q.append((row,col))

                    print("row " + str(row))
                    print("col "+ str(col))
                    count+=1


                    while q:

                        print(q)
                        r,c = q.popleft()
                        if not (r,c) in s:
                            if c < len(grid[row])-1 and grid[r][c+1] == "1":
                                q.append((r,c+1))
                            if c > 0 and grid[r][c-1] == "1":
                                q.append((r,c-1))
                            if r < len(grid)-1 and grid[r+1][c] == "1":
                                q.append((r+1,c))
                            if r >0 and grid[r-1][c] == "1":
                                q.append((r-1,c))

                            s.add((r,c))
                     
        return count



                    




        