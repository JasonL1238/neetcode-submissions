class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.heap = []
        
        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap,i)
            elif i > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap,i)

                

        

    def add(self, val: int) -> int:
        if len(self.heap) < self.size:
            heapq.heappush(self.heap,val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)        
        
        return self.heap[0]
