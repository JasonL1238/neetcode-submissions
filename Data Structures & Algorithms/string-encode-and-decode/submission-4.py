class Solution:

    def encode(self, strs: List[str]) -> str:
            output = []
            for i in range(len(strs)):
                output.append(str(len(strs[i])).zfill(3))
                output.append(strs[i])
            
            word = "".join(output)
            print(word)
            return word


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            length = int(s[i:i+3])
            print(length)
            output.append(s[i+3:i+3+length])
            i += (3+length)
        return output

            
            
