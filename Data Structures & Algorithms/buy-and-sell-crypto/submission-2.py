class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for i in prices:
            minBuy = min(minBuy,i)
            maxProfit = max(maxProfit,i-minBuy)
        
        return maxProfit