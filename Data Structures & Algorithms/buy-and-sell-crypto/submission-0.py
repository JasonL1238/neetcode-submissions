class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        res = 0

        while end < len(prices):
            if(prices[end] - prices[start] > res):
                res = prices[end] - prices[start]
                end+=1
            else:
                if(prices[end] < prices[start]):
                    start = end
                
                end+=1
        
        return res
            