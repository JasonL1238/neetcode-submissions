class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * (n)

        for i in range(1,n):
            dp[i] = max(dp[i-1],nums[i-1]+dp[i-2])

        dp2 = [0] * (n+1)
        for i in range(2,n+1):
            dp2[i] = max(dp2[i-1],nums[i-1]+dp2[i-2])  
        
        return max(dp[n-1],dp2[n])
