class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return amount

        s = {}
        for i in coins:
            s[i] = 1
        
        curr = 0

        def dfs(amount: int):
            if amount in s:
                return s[amount]
            elif amount > 0:
                prev = []
                for i in coins:
                    prev.append(dfs(amount-i))
                best = -1
                for i in prev:
                    if best == -1:
                        best = i
                    elif not i == -1:
                        best = min(i,best)
                
                if best == -1:
                    s[amount] = -1
                    return -1
                s[amount] = best + 1
                return best+1
            return -1                                 
        return dfs(amount)
                
