class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        counts = dict()
        maxLetter = 0
        maxLen = 0

        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1
            

            maxLetter = max(maxLetter,counts[s[r]])
            
            while r-l+1 - maxLetter > k:
                counts[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen,r-l+1)

        
        return maxLen
        

            
            







            
        