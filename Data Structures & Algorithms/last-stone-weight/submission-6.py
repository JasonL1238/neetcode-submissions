class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []


        for i in stones:
            heapq.heappush(heap,-i)

        print(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            diff = first - second

            heapq.heappush(heap,-diff)
        
        return max(heap[0],-heap[0])
