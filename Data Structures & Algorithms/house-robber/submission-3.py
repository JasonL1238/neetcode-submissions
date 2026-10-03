class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)

        def rec(i: int):
            if i <= 0:
                return nums[i]
            elif i == 1:
                return max(nums[0],nums[1])
            else:
                if not dp[i+1] == -1:
                    return dp[i+1]
                dp[i+1] =  max(rec(i-1),rec(i-2)+nums[i])
                return dp[i+1]
        
        return rec(n-1)
