class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = []

        for row in range(numRows+1):
            i = 0
            layer = []
            while i < row:
                if i == 0 or i == row-1:
                    layer.append(1)
                else:
                    prev = i-1
                    prevR = row-1
                    new = output[prevR][prev] + output[prevR][i]
                    layer.append(new)
                i += 1
            output.append(layer.copy())
        output.pop(0)
        return output