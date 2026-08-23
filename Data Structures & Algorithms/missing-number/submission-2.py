class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = 0
        for i in nums:            
            s ^= i
        s2 = 0
        for i in range(len(nums)+1):
            s2 ^= i

        return s2^s

