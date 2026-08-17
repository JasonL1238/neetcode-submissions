class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        m = 0

        while l < r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m 
            else:
                l = m + 1
        
        offset = l

        l = offset
        r = n-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
            
        l = 0
        r = offset-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        
        return -1


                

        
            