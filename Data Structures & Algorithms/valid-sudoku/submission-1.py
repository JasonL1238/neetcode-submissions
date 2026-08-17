class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = set()


        for row in board:
            for col in row:
                if col in rowHash:
                    return False
                elif col.isdigit():
                    rowHash.add(col)
            rowHash.clear()

        col = 0
        row = 0  
        colHash = set()
        sqaureHash = dict()
        while col < 9:
            row=0
            while row < 9:
                if board[row][col] in colHash:
                    print(row)
                    print(col)
                    return False
                elif board[row][col].isdigit():
                    colHash.add(board[row][col])

                square = 3 *(row//3) + (col//3) 
                if square in sqaureHash:
                    if board[row][col] in sqaureHash[square]:
                        print(sqaureHash)
                        return False
                    elif board[row][col].isdigit():
                        sqaureHash[square].add(board[row][col])
                else:
                    sqaureHash[square] = set()
                    if board[row][col].isdigit():
                        sqaureHash[square].add(board[row][col])

                
                row += 1

            col+=1
            colHash.clear()
        



        return True