class Solution:
    def climbStairs(self, n: int) -> int:
        m = {}
        m[n] = 1
        i = n-1


        while i >= 0:
            m[i] = m[i+1]
            if i + 2 <= n:
                m[i] += m[i+2]
            i-=1           
        
        print(m)
        return m[0]



