class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = nums[0]

        i = 1
        dp = [(1,1)] * len(nums)
        dp[0] = (max(1,nums[0]),min(1,nums[0]))

        while i< len(nums):
            num = max(nums[i]*dp[i-1][0],nums[i]*dp[i-1][1])
            num2 = min(nums[i]*dp[i-1][0],nums[i]*dp[i-1][1])
            m = max(num,m)

            dp[i] = (max(num,1),min(num2,1))
            i+=1
        
        return m
