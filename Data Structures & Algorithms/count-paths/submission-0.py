class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        h = dict()

        for r in range(1,m+1):
            for c in range(1,n+1):
                h[(r,c)]=0
        
        h[(1,1)] = 1

        for r in range(1,m+1):
            for c in range(1,n+1):
                if (r-1,c) in h:
                    h[(r,c)] += h[(r-1,c)]
                if (r,c-1)  in h:                  
                    h[(r,c)] += h[(r,c-1)]


        return h[(m,n)]
            