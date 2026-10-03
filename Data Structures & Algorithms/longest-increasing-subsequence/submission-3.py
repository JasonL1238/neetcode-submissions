class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums) 
        dp = [1] * (n)

        for i in range(n):
            for k in range(i+1,n):
                second = nums[k]
                first = nums[i]
                if second > first:
                    dp[k] = max(dp[k],dp[i]+1)
        
        return max(dp)



