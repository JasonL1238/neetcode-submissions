class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = (m*n)//2
        left = 0
        right = m*n - 1

        while left <= right:
            if n == 1:
                col = 0
            else: 
                col = i%n
            row = i//n
            print("i" + str(i) + "row" + str(row) + "col" + str(col))

            if matrix[row][col] == target:
                return True;
            elif matrix[row][col] > target:
                right = i-1
                i = (left+right)//2
            else:
                left = i + 1
                i = (left+right)//2
                print(str(i) + " left ")
        
        return False
        