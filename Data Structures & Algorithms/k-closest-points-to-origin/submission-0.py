class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        x1 = 0
        y1 = 0

        for i in points:
            x2,y2 = i

            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            heapq.heappush(heap,(dist,i))

        output = []
        
        for i in range(k):
            point = heapq.heappop(heap)
            output.append(point[1])
        
        return output


