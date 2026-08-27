class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        curr = 0
        jump = 0

        i = 0
        while i < len(nums)-1:
            num = nums[i]
            jump = max(jump,num)
            if curr == 0:
                curr = jump
                jump = 0
                count +=1
            else:
                jump-=1

            curr-=1
            i+=1
        
        return count
            