class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {len(nums):0}

        i = len(nums)-1
        while i >= 0:
            memo[i] = nums[i]
            if i+2 in memo:
                memo[i] += memo[i+2]
            if i +3 in memo and memo[i+3] > memo[i+2]:
                memo[i] -= memo[i+2]
                memo[i] += memo[i+3]
            i -= 1
        return max(memo[0],memo[1])
