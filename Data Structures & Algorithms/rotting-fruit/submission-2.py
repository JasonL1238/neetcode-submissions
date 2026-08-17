class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        r = set()
        c = set()
        s = set()
        count = 0
        
        change = True

        while change:
            change = False
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    node = grid[row][col]
                    if node == 2 and not (row,col) in s:
                        if row < len(grid)-1 and grid[row+1][col] == 1:
                            grid[row+1][col] =2 
                            s.add((row+1,col))
                            change = True
                        if col < len(grid[0]) -1 and grid[row][col+1] == 1:
                            grid[row][col+1] =2 
                            s.add((row,col+1))
                            change = True
                        if col > 0 and grid[row][col-1] == 1 :
                            grid[row][col-1] = 2
                            s.add((row,col-1))
                            change = True
                        if row > 0 and grid[row-1][col] == 1:
                            grid[row-1][col] = 2
                            s.add((row-1,col))
                            change = True

            count += 1
            print(count)
            print(s)
            print(grid)
            s.clear()   
        

        for i in grid:
            for k in i:
                if k == 1:
                    return -1


        return count-1



