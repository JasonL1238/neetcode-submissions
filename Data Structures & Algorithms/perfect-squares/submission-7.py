import math

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, math.isqrt(n) + 1)]

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break

                dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n]
