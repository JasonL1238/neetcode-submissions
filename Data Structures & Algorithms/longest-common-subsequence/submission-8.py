class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(n+1):
            dp[0][i] = 0
             
        for j in range(m+1):
            dp[j][0] = 0
        
        for row in range(m):
            for col in range(n):
                ch1 = text1[row]
                ch2 = text2[col]

                if ch1 == ch2:
                    dp[row+1][col+1] = max(1+dp[row][col],dp[row][col+1],dp[row+1][col])
                else:
                    dp[row+1][col+1] = max(dp[row][col+1],dp[row+1][col])

        return dp[m][n]
