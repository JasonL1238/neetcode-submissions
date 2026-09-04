class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m = hand[0]
        cards = dict()
        heap = []
        hand.sort()
        
        for i in hand:
            if not i in cards:
                cards[i] = 0
            cards[i] += 1
            heapq.heappush(heap,i)

        while cards:
            while not heap[0] in cards:
                heapq.heappop(heap)
            k = heapq.heappop(heap)
            for i in range(groupSize):
                if k+i in cards:
                    cards[k+i]-=1
                    if cards[k+i] == 0:
                        del cards[k+i]
                    else:
                        m = min(k+i,m)
                else:
                    return False
        
        return True
                

        
        



        
            
        
