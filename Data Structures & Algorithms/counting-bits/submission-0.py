class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n+1)

        for i in range(n+1):
            if i == 0:
                dp[0] = 0
            else:
                dp[i] = dp[i>>1]
                if i & 1:
                    dp[i] += 1
        
        return dp