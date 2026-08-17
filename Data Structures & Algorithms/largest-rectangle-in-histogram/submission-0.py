class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxSingle = heights[0]
        
        stack = []
        leftSpan = [0] * len(heights)
        rightSpan = [0] * len(heights)

        for k in range(len(heights)):
            i = 0
            while len(stack) >= 0:
                if len(stack) == 0:
                    leftSpan[k] = -1
                    break
                top = stack[-1]
                if top[0] < heights[k]:
                    print("top " + str(top) + " k " + str(k))
                    leftSpan[k] = top[1]
                    break
                else:
                    stack.pop()
            stack.append((heights[k],k))

        print(stack)
        stack = []
        for k in range(len(heights)-1, -1, -1):
            while len(stack) >= 0:
                if len(stack) == 0:
                    rightSpan[k] = len(heights)
                    break
                top = stack[-1]
                if top[0] < heights[k]:
                    rightSpan[k] = top[1]
                    break
                else:
                    stack.pop()

            stack.append((heights[k],k))

        print(rightSpan)
        print(leftSpan)
        for k in range(len(heights)):
            height = heights[k]
            area = (rightSpan[k] - leftSpan[k]-1) * height
            maxSingle = max(maxSingle,area)
        
        return maxSingle
            