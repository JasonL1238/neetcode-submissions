class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curr = 0
        bought = -1
        for i in range(len(prices)-1):
            print(curr)
            print(bought)
            if prices[i+1] > prices[i] and bought == -1:
                bought = prices[i]
            elif prices[i+1] < prices[i] and not bought == -1:
                curr += prices[i] - bought
                bought = -1

        if prices[len(prices)-1] > bought and not bought == -1:
                curr += prices[len(prices)-1] - bought
        print("bought" + str(bought))  
        return curr