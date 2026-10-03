class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        m = set(wordDict)
        n = len(s)
        dp = dict()
        

        def rec(l:int, r:int):
            sub = s[l:r]
            if sub in m:
                dp[(l,r)] = True
            elif (l,r) in dp:
                return dp[(l,r)]
            else:
                dp[(l,r)] = False
                for k in range(l+1,r):
                    dp[(l,r)] = dp[(l,r)] or (rec(l,k) and rec (k,r))
            
            return dp[(l,r)]
        
        return rec(0,n)



