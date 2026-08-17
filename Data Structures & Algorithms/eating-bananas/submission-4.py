class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = piles[0]

        for i in piles:
            largest = max(largest,i)

        left = 1
        right = largest
        last = largest
        while left <= right:
            i = (left+right)//2
            iterations = 0
            for k in piles:
                iterations += math.ceil(k/i)
            if iterations <= h:
                print("1. i" + str(i) + "left" + str(left) + "right" + str(right) + " " + str(iterations))
                last = i
                right = i - 1
            else:
                print("2. i" + str(i) + "left" + str(left) + "right" + str(right) + " " + str(iterations))
                left = i + 1

        
        return last

