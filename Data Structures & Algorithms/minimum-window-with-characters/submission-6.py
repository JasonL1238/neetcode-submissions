class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        output = ""
        minLen = float("inf")
        missing = dict()
        numMissing = 0

        for i in t:     
            if i in missing:
                missing[i] += 1
            else:
                missing[i] = 1
        
        numMissing = len(missing.keys())

        for r in range(len(s)): 
            right = s[r]
            if right in missing:
                missing[right] -= 1
                if missing[right] == 0:
                    numMissing -= 1

            while numMissing == 0 and l <= r:
                if r - l + 1 < minLen:
                    output = s[l:r+1]
                    minLen = len(output)

                left = s[l]
                l += 1
                if left in missing:
                    missing[left] += 1
                    if missing[left] == 1:
                        numMissing += 1

        return output
            
            
            



        