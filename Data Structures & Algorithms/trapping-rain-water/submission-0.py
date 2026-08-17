class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]] 
        right = [0] * len(height)
        right[len(height)-1] = height[len(height)-1]

        i = 1
        while i < len(height):
            if height[i] > left[i-1]:
                left.append(height[i])
            else:
                left.append(left[i-1])
            
            if height[len(height)-1-i] > right[len(height)-i]:
                right[len(height)-1-i] = height[len(height)-1-i]
            else:
                right[len(height)-1-i] = right[len(height)-i]
            
            i+=1
        
        print("left: " + str(left))
        print("right: " + str(right))
        res = 0

        for i in range(len(height)):
            if min(left[i],right[i]) - height[i] > 0:
                res += min(left[i],right[i]) - height[i] 
    
        return res