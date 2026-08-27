class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        dp = [[]]
        half = 0
        for i in nums:
            half += i
        if not half%2 == 0:
            return False
        half/=2


        memo = {}
        def dfs(index:int,val:int):
            nonlocal half
            if val == half:
                return True
            if (index,val) in memo:
                return memo[(index,val)]

            if index < len(nums):
                take = dfs(index+1,val+nums[index])
                leave = dfs(index+1,val)
                memo[(index,val)] = take or leave
                return memo[(index,val)]
            return False
        
        return dfs(0,0)

            






        
        