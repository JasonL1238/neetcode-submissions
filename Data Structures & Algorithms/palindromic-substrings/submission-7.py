class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]

        
        for hop in range(len(s)):
            for i in range(len(s)):
                if hop == 0:
                    dp[i][i] = True
                elif hop == 1 and i < len(s)-1:
                    dp[i][i+hop] = s[i] == s[i+hop]
                elif i+hop < len(s):
                    if  s[i] == s[i+hop]:
                        dp[i][i+hop] =  dp[i+1][i+hop-1]
        count = 0

        
        for i in dp:
            for k in i:
                if k:
                    count += 1

        return count
