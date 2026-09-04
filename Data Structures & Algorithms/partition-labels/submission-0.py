class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = dict()

        for i in range(len(s)):
            ch = s[i]
            m[ch] = i
        
        start = 0
        output = []
        end = 0

        for i in range(len(s)):
            ch = s[i]
            end = max(end,m[ch])
            if i == end:
                output.append(end-start+1)
                start = i+1
        
        return output




        

        