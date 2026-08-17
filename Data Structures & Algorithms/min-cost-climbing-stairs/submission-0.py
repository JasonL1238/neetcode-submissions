class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {len(cost):0}

        i = len(cost)-1
        while i >= 0:
            memo[i] = memo[i+1] + cost[i]
            if i+2 in memo:
                memo[i] = min(memo[i],memo[i+2]+cost[i])
            i -= 1
        
        return min(memo[0],memo[1])
