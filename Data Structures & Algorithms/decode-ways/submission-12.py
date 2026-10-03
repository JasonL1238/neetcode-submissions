class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s) == 10:
            return 1
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            num = int(s[i])
            if i == 0:
                dp[i+1] = 1
                if num <= 0:
                    return 0
            else:
                if num > 0:
                    dp[i+1] += dp[i]
                if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) >= 10:
                        print()
                        dp[i+1] += dp[i-1]
            
        print(dp)
        return dp[n]

            