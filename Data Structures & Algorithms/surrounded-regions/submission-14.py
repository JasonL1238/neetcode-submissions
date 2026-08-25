class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def dfs(row:int, col:int):
            visited.add((row,col))
            if row > 0 and board[row-1][col] == "O" and not (row-1,col) in visited:
                dfs(row-1,col)
            if row < len(board)-1 and board[row+1][col] == "O" and not (row+1,col) in visited:
                dfs(row+1,col)
            if col > 0 and board[row][col-1] == "O" and not (row,col-1) in visited:
                dfs(row,col-1)
            if col < len(board[0])-1 and board[row][col+1] == "O" and not (row,col+1) in visited:
                dfs(row,col+1)

        for col in range(len(board[0])):
            if board[0][col] == "O":
                dfs(0,col)
        for col in range(len(board[0])):
            if board[len(board)-1][col] == "O":
                dfs(len(board)-1,col)
        for row in range(len(board)):
            if board[row][0] == "O":
                dfs(row,0)
        for row in range(len(board)):
            if board[row][len(board[0])-1] == "O":
                dfs(row,len(board[0])-1)
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                node = board[row][col]
                if node == "O" and not (row,col) in visited:
                    board[row][col] = "X"

        
