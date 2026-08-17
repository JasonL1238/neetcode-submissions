class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []
        curr = []
        s = 0

        def dfs(i):
            
            nonlocal s
            
            if s == target: 
                output.append(curr.copy())
            
            if s < target:
                s += nums[i]
                curr.append(nums[i])
                dfs(i)

                s -= nums[i]
                curr.pop()
                
                if i < len(nums)-1:
                    dfs(i+1)


            
        dfs(0)

        return output
        
