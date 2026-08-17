class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = dict()

        curr = []

        nums.sort()

        def create(index: int):

            if not tuple(curr) in output:
                output[tuple(curr)] = curr.copy()
            
            if index >= len(nums):
                return
            
            curr.append(nums[index])
            create(index+1)
            curr.pop()
            create(index+1)

        create(0)
        
        return list(output.values())
