class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        k = 0

        for i in nums:
            if k == 0:
                k = i
            else:
                k ^= i
            print(k)
        
        return k

            
