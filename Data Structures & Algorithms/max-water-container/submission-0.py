class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        pointer1 = 0
        pointer2 = len(heights) - 1

        while pointer1 < pointer2:
            cap = min(heights[pointer1],heights[pointer2])
            area = (pointer2-pointer1) * cap
            largest = max(largest,area)
            if heights[pointer1] == cap:
                pointer1 += 1
            else:
                pointer2 -= 1
            
        return largest
        