class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [(0,0)] * (n+1)
        dp[0] = (1,1)
        
        for i in range(n):
            a,b = dp[i]
            a *= nums[i]
            b *= nums[i]
            big = max(a,b,nums[i])
            small = min(a,b,nums[i])
            dp[i+1]= (small,big)

        output = 0
        for i in range(1,n+1):
            output = max(output,dp[i][1])
        return output
            

            

