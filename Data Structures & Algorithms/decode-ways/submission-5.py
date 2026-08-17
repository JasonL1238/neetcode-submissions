class Solution:
    def numDecodings(self, s: str) -> int:

        counts = {}

        for i in range(len(s)):
            counts[i] = 0

        def search(index:int):

            if index < 0:
                return
            
            if int(s[index]) > 0:
                if index < len(s)-1:
                    counts[index] += counts[index+1]
                else:
                    counts[index] += 1

                if index < len(s)-1 and int(s[index])*10+int(s[index+1]) <= 26:
                    if index < len(s)-2:
                        counts[index] += counts[index+2]
                    else:
                        counts[index] += 1

            search(index-1)

            
    
        search(len(s)-1)

        return counts[0]