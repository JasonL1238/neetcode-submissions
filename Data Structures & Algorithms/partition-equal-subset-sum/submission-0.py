class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        dp = [[]]
        half = 0
        for i in nums:
            half += i
        if not half%2 == 0:
            return False
        half/=2



        def dfs(index:int,val:int):
            nonlocal half
            if val == half:
                return True
            if index < len(nums):
                if dfs(index+1,val+nums[index]):
                    return True
                elif dfs(index+1,val):
                    return True
            
            return False
        
        return dfs(0,0)

            






        
        