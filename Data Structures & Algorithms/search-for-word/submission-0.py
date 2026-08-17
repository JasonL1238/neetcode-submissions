class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])
        output = False
        s = set()

        def dfs(r:int,c:int,index:int):
            nonlocal output
            index += 1
            s.add((r,c))

            if index >= len(word):
                output = True
                return
            
            if r<len(board)-1 and board[r+1][c] == word[index] and not (r+1,c) in s:
                dfs(r+1,c,index)
                s.remove((r+1,c))
            if c<len(board[0])-1 and board[r][c+1] == word[index] and not (r,c+1) in s:
                dfs(r,c+1,index)
                s.remove((r,c+1))
            if r>0 and board[r-1][c] == word[index] and not (r-1,c) in s:
                dfs(r-1,c,index)
                s.remove((r-1,c))
            if c>0 and board[r][c-1] == word[index] and not (r,c-1) in s:
                dfs(r,c-1,index)   
                s.remove((r,c-1))             



        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    dfs(row,col,0)
                    s.remove((row,col))

        

        return output


                

        
            

        