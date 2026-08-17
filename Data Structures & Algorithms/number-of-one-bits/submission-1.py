class Solution:
    def hammingWeight(self, n: int) -> int:
        
        l = n.bit_length()

        count = 0
        num = 1
        for i in range(l):
            if not n & num == 0:
                count += 1
            num *= 2
        
        return count