class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        m = nums[0]
        neg = 0
        pos = 0
        curr = nums[0]
        
        i = 1

        while i < len(nums):
            while i < len(nums) and curr + nums[i] > 0:
                curr += nums[i]
                m = max(m,curr)
                i+=1
            print("first" + str(i))
            print(curr)
            while i < len(nums) and nums[i] < curr and nums[i] < 0:
                i+= 1
            if i < len(nums):
                curr = nums[i]
                m = max(m,curr)
                i += 1
            print("second" + str(i))
            print(curr)

        return max(m,curr)

        
                

        



