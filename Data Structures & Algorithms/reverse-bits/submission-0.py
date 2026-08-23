class Solution:
    def reverseBits(self, n: int) -> int:
        i = 31
        output = 0
        while i >= 0:
            if n & 1 == 1:
                output += 2**i
            i-=1
            n>>=1
        return output
