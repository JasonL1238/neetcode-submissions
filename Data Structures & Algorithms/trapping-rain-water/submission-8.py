class Solution:
    def trap(self, height: List[int]) -> int:
        leftForward = [0] * len(height)
        rightForward = [0] * len(height)
        area = 0

        leftMax = 0
        rightMax = 0
        for i in range(len(height)):
            leftMax = max(leftMax,height[i])

            rightIndex = len(height) - i - 1
            rightMax = max(rightMax,height[rightIndex])

            leftForward[i] = leftMax
            rightForward[rightIndex] = rightMax
        
        for i in range(len(height)):
            currMax = min(leftForward[i],rightForward[i])
            if currMax > height[i]:
                area += currMax - height[i]
        
        return area
        
        

