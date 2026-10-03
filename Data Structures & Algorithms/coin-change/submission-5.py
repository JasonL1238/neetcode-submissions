class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        cache = dict()
        s = set(coins)

        def rec(target:int):
            if target in cache:
                return cache[target]

            if target <= 0:
                return float("inf")
            elif target in s:
                cache[target] = 1
            else:
                best = float("inf")
                for i in coins:
                    t = target - i
                    best = min(best,rec(t))
                if best == float("inf"):
                    cache[target] = float("inf")
                else:
                    cache[target] = best + 1

            return cache[target]
        
        print(cache)
        output = rec(amount)
        if output == float("inf"):
            return -1
        return output
