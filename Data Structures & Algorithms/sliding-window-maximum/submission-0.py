import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        i = 0
        output = []
        heap = []

        while i < k:
            if i >= len(nums):
                return [-heap[0][0]]
            elem = (-nums[i],i)
            heapq.heappush(heap,elem)
            i+=1
        
        top = heap[0]
        output.append(-top[0])

        l = 1
        r = k
        while r < len(nums):
            elem = (-nums[r],r)
            heapq.heappush(heap,elem)

            top = heap[0]
            while top[1] < l:
                heapq.heappop(heap)
                top = heap[0]
        
            output.append(-top[0])

            r+=1
            l+=1
            
        return output


            
