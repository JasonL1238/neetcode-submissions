class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0

        i = 0

        while i < len(nums)-1:
            curr = max(nums[i],curr)
            if curr == 0:
                return False
            i += 1
            curr -= 1
        
        return True

    


       

        
