class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        m = dict()
        n = len(s)
        memo = dict()
        for i in wordDict:
            m[i] = True

        def dfs(index:int):
            i = 0
            curr = ""
            if s[index:n] in m:
                return True
            if index in memo:
                return memo[index]
            
            while index+i < n:
                curr += s[index+i]
                if curr in m:
                    if index + i + 1 in memo:
                        return memo[index + i + 1]
                    if dfs(i+index+1):
                        memo[index] = True
                        return True
                i += 1

            memo[index] = False
            return False
        
        return dfs(0)