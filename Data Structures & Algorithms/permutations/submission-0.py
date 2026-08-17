class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        outputs = []

        curr = []
        s = set()

        def create() -> None:
            if len(s) == len(nums):
                outputs.append(curr.copy()) 
            else:
                for i in range(len(nums)):
                    if not i in s:
                        curr.append(nums[i])
                        s.add(i)
                        create()
                        s.remove(i)
                        curr.pop()
                
        create()
        return outputs
