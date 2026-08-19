class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        output = ""
        i = 0 

        while i < len(s):
            l = i -1
            r = i +1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l+=1
            r-=1

            if len(output) < r-l+1:
                output = s[l:r+1]
            i+=1
            

        l = 0
        r = 1
        while r < len(s):
            prevl = l
            prevr = r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l+=1
            r-=1
            if len(output) < r-l+1:
                output = s[l:r+1]
            l = prevl+1
            r = prevr+1
        
        return output
        


