class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        first = [0] * 26
        live = [0] * 26

        for i in s1:
            index = ord(i) - ord("a")
            first[index] += 1

        for i in range(len(s1)-1):
            index = ord(s2[i]) - ord("a")
            live[index] += 1       

        
        while r < len(s2):
            index = ord(s2[r]) - ord("a")
            print(index)
            live[index] = max(0,live[index]+1)
            print(live)
            if live == first:
                return True
            else:
                index = ord(s2[l]) - ord("a")
                live[index] = max(0,live[index]-1)
                l += 1
                
            r += 1

        return False


        